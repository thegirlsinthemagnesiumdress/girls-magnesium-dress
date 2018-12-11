import hashlib

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from djangae.fields import JSONField
from django.conf import settings
from django.db import models
from django.urls import reverse
from uuid import uuid4


SURVEY_URL = 'https://google.qualtrics.com/jfe/form/{}'.format(settings.QUALTRICS_SURVEY_ID)


class User(GaeAbstractDatastoreUser):

    @property
    def is_whitelisted(self):
        """
        Returns `True` if email is in `settings.WHITELISTED_USERS` list,
        `False` otherwise.
        """
        return True if self.email in settings.WHITELISTED_USERS else False

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
    industry = models.CharField(max_length=128, choices=settings.INDUSTRIES.iteritems())
    country = models.CharField(max_length=2, choices=settings.COUNTRIES.iteritems())
    last_survey_result = models.ForeignKey('SurveyResult', null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def link(self):
        """
        Lint to qualtrics survey. Every company will have a different URL, created
        out of the sid.
        The sid will be stored for every survey response and we will be able to use
        it to match the data against companies.
        """
        return '{}?sid={}'.format(SURVEY_URL, self.sid)

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

        self.industry = self.industry if self.industry in settings.INDUSTRIES.keys() else None
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
