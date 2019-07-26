from django.template.defaulttags import register
from django.utils import translation


@register.filter(name="strip_lang")
def strip_lang(value):
    lang = translation.get_language()
    return value.replace('/{0}/'.format(lang), '/')
