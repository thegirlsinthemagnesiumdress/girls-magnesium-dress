from django.conf import settings

from core.models import Survey


def migrate_to_default_tenant():
    default_tenant = settings.DEFAULT_TENANT

    Survey.objects.update(tenant=default_tenant)
