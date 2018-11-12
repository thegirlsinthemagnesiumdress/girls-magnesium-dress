import json
import logging

from os.path import join
from urlparse import urljoin

from django import template
from django.conf import settings

register = template.Library()


def _get_manifest():
    if not getattr(_get_manifest, "_MANIFEST", None):
        with open(join(settings.STATIC_ROOT, "rev-manifest.json")) as f:
            _get_manifest.MANIFEST = json.loads(f.read())
    return _get_manifest.MANIFEST


_get_manifest.MANIFEST = None


@register.simple_tag
def static_rev(path):
    try:
        manifest = _get_manifest()
    except IOError:
        # Not sure this is the right behaviour, probably should have its
        # own flag in settings rather than relying on DEBUG
        if not settings.DEBUG:
            logging.warning("Unable to find asset manifest, paths may be incorrect")

        return urljoin(settings.STATIC_URL, path)

    return urljoin(settings.STATIC_URL, manifest[path])
