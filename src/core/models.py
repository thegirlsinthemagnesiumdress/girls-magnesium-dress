import hashlib

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from djangae.fields import JSONField
from django.conf import settings
from django.db import models
from django.urls import reverse
from uuid import uuid4
from core.conf.utils import flatten
from core.settings.tenants import TENANTS_CHOICES


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
    DMB_overall_average_by_dimension:
    {
        [category]: benchmark
    }
    """

    sid = models.CharField(primary_key=True, editable=False, max_length=32)
    company_name = models.CharField(max_length=50)
    engagement_lead = models.CharField(max_length=32, blank=True, null=True)
    industry = models.CharField(max_length=128, choices=flatten(settings.HIERARCHICAL_INDUSTRIES))
    country = models.CharField(max_length=2, choices=settings.COUNTRIES.iteritems())
    last_survey_result = models.ForeignKey('SurveyResult', null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    tenant = models.CharField(max_length=128, choices=TENANTS_CHOICES)

    @property
    def link(self):
        """
        Lint to qualtrics survey. Every company will have a different URL, created
        out of the sid.
        The sid will be stored for every survey response and we will be able to use
        it to match the data against companies.
        """
        qualtrics_survey_id = settings.TENANTS.get(self.tenant).get('QUALTRICS_SURVEY_ID')
        survey_url = 'https://google.qualtrics.com/jfe/form/{}'.format(qualtrics_survey_id)
        return '{}?sid={}'.format(survey_url, self.sid)

    @property
    def link_sponsor(self):
        """
        We need to differenziate between sponsor (survey creators)
        amd participants. The way that is done is by setting sp=true.
        """
        return '{}&sp=true'.format(self.link)

    @property
    def last_survey_result_link(self):
        return reverse('report', kwargs={'sid': self.sid}) if self.last_survey_result else None

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sid = uuid4().hex

        assert self.industry in settings.INDUSTRIES.keys()
        assert self.country in settings.COUNTRIES.keys()
        # assert self.tenant in settings.TENANTS.keys()

        super(Survey, self).save(*args, **kwargs)


class SurveyResult(models.Model):
    """Model to store a survey response benchmark."""

    survey = models.ForeignKey('Survey', null=True, related_name="survey_results")
    response_id = models.CharField(max_length=50, unique=True)
    loaded_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()
    excluded_from_best_practice = models.BooleanField(default=False)

    dmb = models.DecimalField(max_digits=4, decimal_places=2)
    dmb_d = JSONField()
    raw = JSONField()
    survey_definition = models.ForeignKey('SurveyDefinition', null=True, related_name="survey_definition")

    @property
    def report_link(self):
        return reverse('report_result', kwargs={'response_id': self.response_id})

    @property
    def detail_link(self):
        return reverse(
            'result-detail',
            kwargs={'response_id': self.response_id}) if self.raw and self.survey_definition else None


class SurveyDefinition(models.Model):
    last_modified = models.DateTimeField()
    content = JSONField()
