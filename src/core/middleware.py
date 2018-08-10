import logging

from djangae import environment
from django.conf import settings
from django.http import HttpResponseForbidden


class DomainRestrictionMiddleware(object):
    """Middleware to allow access to authenticated users in ALLOWED_AUTH_DOMAINS."""
    def process_request(self, request):
        if environment.is_in_task() or environment.is_in_cron():
            # Tasks should be allowed through
            logging.info("Allowing task through domain restriction")
            return

        if request.user.is_authenticated():
            ALLOWED_AUTH_DOMAINS = getattr(settings, "ALLOWED_AUTH_DOMAINS", [])  # noqa
            domain = request.user.email.split("@")[-1]
            if domain not in ALLOWED_AUTH_DOMAINS and '*' not in ALLOWED_AUTH_DOMAINS:
                return HttpResponseForbidden("User is not on a valid domain")
        else:
            return HttpResponseForbidden("User is not on a valid domain")
