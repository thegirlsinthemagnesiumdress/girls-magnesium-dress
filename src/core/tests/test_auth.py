from core.settings.staging import MIDDLEWARE_CLASSES
from core.test import with_appengine_anon, with_appengine_user
from djangae.test import TestCase
from django.conf.urls import include, url
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.test import override_settings


@login_required
def logged_in_view(request):
    return HttpResponse("OK")


def public_view(request):
    return HttpResponse("OK")


urlpatterns = [
    url("^$", lambda req: HttpResponse("OK")),
    url("^logged_in_view/$", logged_in_view),
    url("^public_view/$", public_view),
    url(r'^gauth/', include('djangae.contrib.gauth.urls'))
]


@override_settings(
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES)
class DomainRestrictionMiddlewareTests(TestCase):
    """Test class for `core.middleware.DomainRestrictionMiddleware`."""

    def setUp(self):
        # A bounch of users are created in the backend
        User = get_user_model()  # noqa

        User.objects.create(email='test@google.com')
        User.objects.create(email='test@example.com')

    @with_appengine_user(email='test@gmail.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["google.com"])
    def test_users_restricted_by_domain_not_allowed(self):
        """When a user is not in ALLOWED_AUTH_DOMAINS returns 403."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_user(email='test@google.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["google.com"])
    def test_users_restricted_by_domain_allowed(self):
        """When a user is in ALLOWED_AUTH_DOMAINS returns 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    @with_appengine_user(email='test@example.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["google.com"])
    def test_existing_users_restricted_by_domain(self):
        """When a user exists and it is not in ALLOWED_AUTH_DOMAINS returns 403."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_anon
    @override_settings(ALLOWED_AUTH_DOMAINS=["google.com"])
    def test_domain_restriction_not_allows_anonymous_users(self):
        """Anonymous users are not accepted. returns 403."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_anon
    @override_settings(ALLOWED_AUTH_DOMAINS=["*"])
    def test_domain_star_not_allows_anonymous_users(self):
        """Anonymous users are not accepted, even with domain *. returns 403."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_user(email='test@example.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["*"])
    def test_domain_star_allows_example_domain(self):
        """When ALLOWED_AUTH_DOMAINS is *, any registered user is accepted. returns 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    @with_appengine_user(email='test@gmail.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["*"])
    def test_domain_star_only_allows_registered_users(self):
        """
        When ALLOWED_AUTH_DOMAINS is *, any registered user is accepted,
        but test@gmail.com is not, so returns 403.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_anon
    @override_settings(ALLOWED_AUTH_DOMAINS=["*"])
    def test_login_required_page_anon_user_access_denied(self):
        """
        A login required page for anonymous user, even when ALLOWED_AUTH_DOMAINS is *,
        the access is denied. Returns 403.
        """
        response = self.client.get("/logged_in_view/")
        self.assertEqual(response.status_code, 403)

    @with_appengine_user(email='test@example.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["*"])
    def test_loging_required_valid_user_star_domain(self):
        """For a valid user, when ALLOWED_AUTH_DOMAINS is * and the view is login required, returns 200."""
        response = self.client.get("/logged_in_view/")
        self.assertEqual(response.status_code, 200)

    @with_appengine_user(email='test@example.com')
    @override_settings(ALLOWED_AUTH_DOMAINS=["google"])
    def test_loging_required_valid_user_is_not_in_allowed_domain(self):
        """For a valid user that is not in ALLOWED_AUTH_DOMAINS, access is denied."""
        response = self.client.get("/logged_in_view/")
        self.assertEqual(response.status_code, 403)
