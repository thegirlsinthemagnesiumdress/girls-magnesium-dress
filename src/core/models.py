from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from django.db import models
from  django.utils import timezone
import hashlib
import datetime


class User(GaeAbstractDatastoreUser):
    is_qualtrics=models.BooleanField(default=False)

SURVEY_URL = 'https://google.qualtrics.com/jfe/form/SV_beH0HTFtnk4A5rD'

class Survey(models.Model):
    company_name= models.CharField(max_length=50)
    uid = models.CharField(unique=True, editable=False, max_length=32)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def link(self):
        """
        Lint to qualtrics survey. Every company will have a different URL, created
        out of the uid.
        The uid will be stored for every response and we will be able to used that
        id to match the data against companies.
        """
        return '{}?sid={}'.format(SURVEY_URL, self.uid)

    @property
    def link_sponsor(self):
        """
        We need to differenziate between sponsor (survey creators)
        amd participants. The way that is done is by setting sp=true.
        """
        return '{}&sp=true'.format(self.link)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
            m = hashlib.md5()
            md5 = m.update(self.company_name + self.created_at.isoformat())
            self.uid = m.hexdigest()
        super(Survey, self).save(*args, **kwargs)
