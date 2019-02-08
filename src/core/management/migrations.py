from core.models import Survey
from django.conf import settings


def migrate_to_tenant():
    Survey.objects.update(tenant=settings.ADS)
