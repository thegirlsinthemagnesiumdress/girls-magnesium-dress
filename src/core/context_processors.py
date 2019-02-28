from django.core.urlresolvers import resolve
from django.conf import settings
from core.conf.utils import get_tenant_key


def tenant_details(request, *args, **kwargs):
    match = resolve(request.path)
    tenant = match.kwargs.get('tenant')
    if tenant:
        tenant_key = get_tenant_key(tenant)
        dimensions = settings.TENANTS[tenant_key]['DIMENSION_TITLES']
        return {
            'tenant_key': tenant_key,
            'dimensions': dimensions,
        }

    return {}
