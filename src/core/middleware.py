import logging

from djangae import environment
from django.conf import settings
from django.http import HttpResponseForbidden
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth.views import redirect_to_login


def is_login_url(request):
    login_url = reverse(settings.LOGIN_URL)
    return request.get_full_path().startswith(login_url)


class DomainRestrictionMiddleware(object):
    """Middleware to allow access to authenticated users in ALLOWED_AUTH_DOMAINS."""
    def process_request(self, request):
        if environment.is_in_task() or environment.is_in_cron():
            # Tasks should be allowed through
            logging.info("Allowing task through domain restriction")
            return

        view = resolve(request.path)

        # Allow decorators on views to bypass this to do their own
        # handling (this is mainly for allowing API access to inbound App Engine
        # Apps)
        if getattr(view.func, "_bypass_domain_restriction", False):
            return

        if not request.user.is_authenticated():
            if is_login_url(request):
                # Ignore the login URL from this redirect to prevent an infinite redirect loop
                return
            else:
                logging.info("Redirecting user to login")
                print("AAAAAAAA")
                return redirect_to_login(request.get_full_path())

        ALLOWED_AUTH_DOMAINS = getattr(settings, "ALLOWED_AUTH_DOMAINS", [])  # noqa

        domain = request.user.email.split("@")[-1]
        print('domain ===> ', domain)
        if domain not in ALLOWED_AUTH_DOMAINS and '*' not in ALLOWED_AUTH_DOMAINS:
            return HttpResponseForbidden("User is not on a valid domain")
