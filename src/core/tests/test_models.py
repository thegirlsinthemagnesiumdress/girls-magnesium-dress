# -*- coding: utf-8 -*-
import re

from core.models import Survey, User
from core.tests.mommy_recepies import make_survey
from core.tests.mocks import MOCKED_TENANTS
from djangae.test import TestCase
from django.test import override_settings
from core.tests.mommy_recepies import make_user
from core.test import with_appengine_admin, with_appengine_user


@override_settings(
    TENANTS=MOCKED_TENANTS
)
class SurveyTest(TestCase):
    """Test case for `core.Survey` model."""

    # def setUp(self):
    #     self.surveys = make_survey(_quantity=3)

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

    @override_settings(
        INDUSTRIES={
            'IT': 'Information Technology',
        }
    )
    def test_save_valid_industry(self):
        """Saving an industry that is in industry list, should set industry field to that industry."""
        survey = Survey.objects.create(country='IT', industry='IT', tenant='tenant1')
        self.assertEqual(survey.industry, 'IT')

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
