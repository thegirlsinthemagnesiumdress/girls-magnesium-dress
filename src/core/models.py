import hashlib

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from djangae.fields import JSONField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import translation
from uuid import uuid4
from core.settings.tenants import TENANTS_CHOICES
from core.settings.default import QUALTRICS_LANGS_REV
from core.managers import NotExcludedFromBestPracticeManager
from core.conf import utils
from collections import OrderedDict


class User(GaeAbstractDatastoreUser):

    @property
    def is_super_admin(self):
        """
        Returns `True` if the user is set in the admin console and is a googler
        `False` otherwise.
        """
        domain = self.email.split("@")[-1]
        return True if self.is_superuser and domain == "google.com" else False

    @property
    def engagement_lead(self):
        """Returns MD5 of email field."""
        m = hashlib.md5()
        m.update(self.email.encode('utf-8'))
        return m.hexdigest()


class Survey(models.Model):
    """
    Models the surveys (internal and external)
    related to an individual company/division.

    fields:
        sid (char[32], Primary Key): The ID of the survey instance.
        company_name (char[50], Required): The name of the comapny/division.
        engagement_lead (char[32], Optional): The LDAP of engagement lead Googler.
        industry (char[128], Required): The industry of the company/division.
        country (char[2], Required): The country code of the country that the compand/division exists in.
        last_survey_result (ForeignKey, Optional): SID of the last external survey taken.
        last_internal_result (ForeignKey, Optional): SID of the last internal survey taken.
        created_at (DateTime, Auto-Generated): The time when the survey model was created.
        tenant (char[128], Required): The associated tenant for this survey (ads, news, retail, etc.).
        account_id (char[64], Optional): The internal Google ID for the company associated with this survey.
        parent_id (char[64], Optional): The internal Google ID for the parent company of the company associated with
                                        this survey.
    """

    sid = models.CharField(primary_key=True, editable=False, max_length=32)
    company_name = models.CharField(max_length=50)
    engagement_lead = models.CharField(max_length=32, blank=True, null=True)
    industry = models.CharField(max_length=128)
    country = models.CharField(max_length=2, choices=settings.COUNTRIES.iteritems())
    last_survey_result = models.ForeignKey('SurveyResult', null=True, related_name='+')
    last_internal_result = models.ForeignKey('SurveyResult', null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    tenant = models.CharField(max_length=128, choices=TENANTS_CHOICES)
    account_id = models.CharField(max_length=64, blank=True, null=True)
    parent_id = models.CharField(max_length=64, blank=True, null=True)

    def get_industry_display(self, *args, **kwargs):
        t = settings.TENANTS[self.tenant]
        industries_dict = OrderedDict(utils.flatten(t['HIERARCHICAL_INDUSTRIES']))
        industry = industries_dict.get(self.industry)
        return industry if industry else None

    def build_qualtrics_link(self, qualtrics_survey_id, i18n=False):
        """
        Builds a qualtrics link for a specified qualtrics survey
        and adds parameter values for the relevant version
        or internationalization.

        Args:
            qualtrics_survey_id (str): ID of qualtrics survey to link to.
            i18n (bool, optional): Does the survey support i18n. Defaults to False.

        Returns:
            str: Link to the relevant survey with parameter values set.
        """
        qualtrics_survey_id = settings.TENANTS.get(self.tenant).get('QUALTRICS_SURVEY_ID')
        version, is_nightly, is_development = utils.version_info(settings.HTTP_HOST)

        if is_nightly or is_development:
            survey_link = settings.QUALTRICS_BASE_SURVEY_PREVIEW_URL.format(survey_id=qualtrics_survey_id, sid=self.sid)
        else:
            survey_link = settings.QUALTRICS_BASE_SURVEY_URL.format(survey_id=qualtrics_survey_id, sid=self.sid)

        if version:
            survey_link = '{}&ver={}'.format(survey_link, version)

        if i18n:
            # Append the qualtrics language code if tenant uses il8n using the browser language code
            survey_link = '{}&Q_Language={}'.format(survey_link, QUALTRICS_LANGS_REV[str(translation.get_language())])

        return survey_link

    @property
    def link(self):
        """
        Link to qualtrics survey. Every company will have a different URL, created
        out of the sid.
        The sid will be stored for every survey response and we will be able to use
        it to match the data against companies.
        """
        qualtrics_survey_id = settings.TENANTS.get(self.tenant).get('QUALTRICS_SURVEY_ID')
        i18n = settings.TENANTS.get(self.tenant).get('i18n')
        survey_link = self.build_qualtrics_link(qualtrics_survey_id, i18n)

        return survey_link

    @property
    def internal_link(self):
        """
        Link to internal qualtrics survey. Every company will have a different URL,
        created out of the sid.
        The sid will be stored for every survey response and we will be able to use
        it to match the data against companies.
        """
        internal_tenant = settings.INTERNAL_TENANTS.get(self.internal_slug)
        if internal_tenant is None:
            raise Exception(
                'Internal link requested from tenant ({}) with no internal counterpart.'
                .format(settings.TENANTS.get(self.slug))
            )
        qualtrics_survey_id = internal_tenant.get('QUALTRICS_SURVEY_ID')
        return self.build_qualtrics_link(qualtrics_survey_id)

    @property
    def link_sponsor(self):
        """
        We need to differenziate between sponsor (survey creators)
        amd participants. The way that is done is by setting sp=true.
        """
        return '{}&sp=true'.format(self.link)

    @property
    def last_survey_result_link(self):
        return reverse('report', kwargs={
            'tenant': self.slug,
            'sid': self.sid
        }) if self.last_survey_result_id else None

    @property
    def last_internal_result_link(self):
        return reverse('report', kwargs={
            'tenant': self.slug,
            'sid': self.sid
        }) if self.last_internal_result_id else None

    @property
    def slug(self):
        return utils.get_tenant_slug(self.tenant)

    @property
    def internal_slug(self):
        return utils.get_tenant_slug(self.tenant) + '_internal'

    @property
    def excluded(self):
        return self.last_survey_result.excluded_from_best_practice if self.last_survey_result else True

    @property
    def internal_excluded(self):
        return self.last_internal_result.excluded_from_best_practice if self.last_internal_result else True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sid = uuid4().hex

        assert self.country in settings.COUNTRIES.keys(), "%r is not in set of configured COUNTRIES" % self.country
        assert self.tenant in settings.TENANTS.keys(), "%r is not in set of configured TENANTS" % self.tenant

        industry_list = settings.TENANTS[self.tenant]['INDUSTRIES'].keys()
        assert self.industry in industry_list, "%r is not in set of configured INDUSTRIES" % self.industry

        super(Survey, self).save(*args, **kwargs)


class SurveyResult(models.Model):
    """
    Model to store a survey response benchmark.

    fields:
        survey (ForeignKey, Optional): The survey model (company) which this set of results is associated with.
        internal_survey (ForeignKey, Optional): The survey model (same as above) which the internal results are
                                               associated with.
        response_id (char[50], Primary Key): The ID of this particular response.
        loaded_at (DateTime, autogenerated): The time at which this set of results was loaded.
        started_at (DateTime): The time at which this survay which produced these results was started.
        excluded_from_best_practice (Boolean, Optional): Was this survey invalid since it was completed too quickly?
        dmb (Decimal): The overall result of the survey (the Digital Maturity Benchmark of the company).
        dmb_d (JSON): The scores for each of the digital matrurity benchmark dimensions.
        raw: (JSON): The raw survey result data from qualtrics.
        survey_definition (ForeignKey, Optional): The content of the survey (questions, dimensions, etc.).
        valid_results (Manager): Used for determining which results need to be excluded from calculations.
    """

    survey = models.ForeignKey('Survey', null=True, related_name="survey_results")
    internal_survey = models.ForeignKey('Survey', null=True, related_name="internal_results")
    response_id = models.CharField(max_length=50, unique=True)
    loaded_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()
    excluded_from_best_practice = models.BooleanField(default=False)

    dmb = models.DecimalField(max_digits=4, decimal_places=2)
    dmb_d = JSONField()
    raw = JSONField()
    survey_definition = models.ForeignKey('SurveyDefinition', null=True, related_name="survey_definition")

    objects = models.Manager()
    valid_results = NotExcludedFromBestPracticeManager()

    @property
    def report_link(self):
        return reverse('report_result', kwargs={'tenant': self.survey.slug, 'response_id': self.response_id})

    @property
    def detail_link(self):
        if not self.raw:
            return None

        if not self.survey_definition_id:
            return None

        return reverse(
            'result-detail',
            kwargs={
                'tenant': self.survey.slug,
                'response_id': self.response_id,
            },
        )

    @property
    def absolute_report_link(self):
        return "http://{}{}".format(settings.DOMAIN, self.report_link)

    @property
    def absolute_detail_link(self):
        return "http://{}{}".format(settings.DOMAIN, self.detail_link)

    class Meta:
        ordering = ('-started_at',)


class SurveyDefinition(models.Model):
    """
    fields:
        tenant (char[128], Required): The tenant associated with this survey definition.
        last_modified (DateTime): The last time this definition was modified.
        content (JSON): The questions and answers for the survey and comparing on the ResultsDetail page.
    """
    tenant = models.CharField(max_length=128, choices=TENANTS_CHOICES)
    last_modified = models.DateTimeField()
    content = JSONField()


class IndustryBenchmark(models.Model):
    industry = models.CharField(max_length=128)
    tenant = models.CharField(max_length=128, choices=TENANTS_CHOICES)
    initial_dmb = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    initial_dmb_d = JSONField(null=True)
    initial_best_practice = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    initial_best_practice_d = JSONField(null=True)
    sample_size = models.IntegerField(null=True)

    dmb_value = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    dmb_d_value = JSONField(null=True)
    dmb_bp_value = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    dmb_d_bp_value = JSONField(null=True)

    class Meta:
        unique_together = (("industry", "tenant"),)
