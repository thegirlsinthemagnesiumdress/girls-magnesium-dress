from django.template.defaulttags import register
from django.utils.translation import get_language
from django.conf import settings


@register.simple_tag
def static_i18n(path):
    if get_language() != 'en':
        return '{}img/{}/{}'.format(settings.STATIC_URL, get_language(), path)
    else:
        return '{}img/{}'.format(settings.STATIC_URL, path)
