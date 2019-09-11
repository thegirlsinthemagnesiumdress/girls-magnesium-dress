# -*- coding: utf-8 -*-
import re

from core.models import Survey, User
from core.tests.mommy_recepies import make_survey
from core.tests.mocks import MOCKED_TENANTS, MOCKED_INTERNAL_TENANTS
from djangae.test import TestCase
from django.test import override_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser
from core.tests.mommy_recepies import make_user
from core.test import with_appengine_admin, with_appengine_user


@override_settings(
    TENANTS=MOCKED_TENANTS,
    INTERNAL_TENANTS=MOCKED_INTERNAL_TENANTS
)
class SurveyTest(TestCase):
    """Test case for `core.Survey` model."""

    def test_uid_is_generated_on_save(self):
        """Test that the survey generates a sid on save."""
        s = Survey(company_name="test", country="IT", industry="re", tenant="tenant1")
        self.assertFalse(s.sid)
        s.save()
        self.assertTrue(s.sid)

    def test_link(self):
        """
        Test that the link has the sid set
        in the query string,
        """
        survey = make_survey()
        match = re.search(r'sid=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], survey.sid)

    def test_internal_link(self):
        """
        Test that the internal survey link
        has the correct survey ID.
        """
        survey = make_survey(tenant="tenant1")
        internal_tenant = MOCKED_INTERNAL_TENANTS[survey.tenant]
        match = re.search(r'preview/([^&]*)[?]', survey.internal_link)
        self.assertEqual(match.groups(1)[0], internal_tenant.get('QUALTRICS_SURVEY_ID'))

    def test_no_internal_link(self):
        """
        Test that a tenant with no internal
        counterpart does not have a
        internal link.
        """
        survey = make_survey(tenant="tenant2")
        # Test that no internal tenant exists
        internal_tenant = MOCKED_INTERNAL_TENANTS.get(survey.slug)
        self.assertEqual(None, internal_tenant)
        # Check that if a survey link is requested None is returned
        self.assertEqual(None, survey.internal_link)

    def test_i18n_link(self):
        """
        Test that a link is set with the
        correct language code
        """
        survey = Survey(company_name="i18n-test", country="EN", industry="re", tenant="tenant1")
        match = re.search(r'Q_Language=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], 'EN')

    def test_sponsor_link(self):
        """
        Test that the sponsor link has both the sid and sponsor flag
        in the query string,
        """
        survey = make_survey()
        match = re.search(r'sid=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], survey.sid)
        match = re.search(r'sp=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], 'true')

    def test_save_valid_industry(self):
        """Saving an industry that is in industry list, should set industry field to that industry."""
        survey = Survey.objects.create(country='IT', industry="re", tenant='tenant1')
        self.assertEqual(survey.industry, 're')
        self.assertEqual(survey.get_industry_display(), "Real estate")

    def test_company_name_unicode(self):
        """Test that company name can have unicode characters."""
        unicode_company_name = u"Company name unicode Æ"
        s = Survey(company_name=unicode_company_name, country="IT", industry="re", tenant='tenant1')
        s.save()
        self.assertTrue(s.sid)
        survey = Survey.objects.get(sid=s.sid)
        self.assertEqual(unicode_company_name, survey.company_name)

    def test_save_valid_tenant(self):
        """Saving a tenant that is in tenant list, should set tenant field to that tenant."""
        survey = Survey.objects.create(company_name="test", country="IT", industry="re", tenant='tenant1')
        self.assertEqual(survey.tenant, 'tenant1')

    def test_save_invalid_tenant(self):
        """Saving a tenant that is not in tenant list, should raise AssertionError."""
        self.assertRaises(Survey.objects.create, company_name="test", country="IT", industry="re", tenant='tenant3')


class UserTest(TestCase):

    def test_user_unicode(self):
        unicode_email = u"MÆrk@gmail.com"
        email_hashed = "7f0a491dd059f5b0432c5485f639b645"
        make_user(email=unicode_email)

        self.assertEqual(User.objects.count(), 1)

        stored_user = User.objects.get(email=unicode_email)

        self.assertEqual(stored_user.engagement_lead, email_hashed)
        self.assertEqual(stored_user.email, unicode_email)

    def test_regular_user(self):
        unicode_email = "user@gmail.com"
        email_hashed = "cba1f2d695a5ca39ee6f343297a761a4"
        make_user(email=unicode_email)

        self.assertEqual(User.objects.count(), 1)

        stored_user = User.objects.get(email=unicode_email)

        self.assertEqual(stored_user.engagement_lead, email_hashed)
        self.assertEqual(stored_user.email, unicode_email)

    @with_appengine_user('standard@asd.com')
    def test_standard_user_not_super_admin(self):
        response = self.client.get('/')
        user = response.wsgi_request.user
        self.assertFalse(user.is_super_admin)

    @with_appengine_user('standard@google.com')
    def test_standard_google_user_not_super_admin(self):
        response = self.client.get('/')
        user = response.wsgi_request.user
        self.assertFalse(user.is_super_admin)

    @with_appengine_admin('standard@gmail.com')
    def test_superuser_not_google_not_super_admin(self):
        response = self.client.get('/')
        user = response.wsgi_request.user
        self.assertFalse(user.is_super_admin)

    @with_appengine_admin('standard@google.com')
    def test_superuser_google_not_super_admin(self):
        response = self.client.get('/')
        user = response.wsgi_request.user
        self.assertTrue(user.is_super_admin)

    @with_appengine_admin('standard@google.com')
    def test_admin_created_survey_links_to_user(self):
        data = {
            'company_name': 'test company',
            'industry': 'ic-o',
            'country': 'GB',
            'tenant': 'ads',
        }
        url = reverse('create_survey')
        response = self.client.post(url, data)
        user = response.wsgi_request.user

        user_survey = Survey.objects.first()
        anon_survey = make_survey()
        make_survey()

        self.assertEqual(user_survey.creator, user)
        self.assertEqual(anon_survey.creator, None)
        self.assertEqual(user.accounts.count(), 1)
