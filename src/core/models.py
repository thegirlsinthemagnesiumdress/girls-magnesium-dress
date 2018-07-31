import hashlib

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from djangae.fields import JSONField
from django.db import models
from django.utils import timezone


SURVEY_URL = 'https://google.qualtrics.com/jfe/form/SV_beH0HTFtnk4A5rD'


class User(GaeAbstractDatastoreUser):
    pass


class Survey(models.Model):
    """
    DMB_overall_average_by_dimension:
    {
        [category]: benchmark
    }
    """

    sid = models.CharField(primary_key=True, editable=False, max_length=32)
    company_name = models.CharField(max_length=50)
    engagement_lead = models.CharField(max_length=32, null=True)

    # Timestamps
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

    def get_dmb_overall_by_dimension(self, dimension):
        self.DMB_overall_average_by_dimension.get(dimension)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            m = hashlib.md5()
            m.update(self.company_name + self.created_at.isoformat())
            self.sid = m.hexdigest()
        super(Survey, self).save(*args, **kwargs)


class SurveyResult(models.Model):
    """Model to store a survey response benchmark."""

    survey = models.ForeignKey(Survey, null=True)
    response_id = models.CharField(max_length=50)
    loaded_at = models.DateTimeField(auto_now_add=True)

    dmb = models.DecimalField(max_digits=4, decimal_places=2)
    dmb_d = JSONField()
