from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from django.db import models
from  django.utils import timezone
import hashlib
import datetime


class User(GaeAbstractDatastoreUser):
    pass

class Company(models.Model):
    uuid = models.CharField(unique=True, editable=False)
    company_name= models.CharField(max_length=50)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
            m = hashlib.md5()
            md5 = m.update(self.company_name + self.created_at.isoformat())
            self.uuid = m.hexdigest()
        super(Company, self).save(*args, **kwargs)
