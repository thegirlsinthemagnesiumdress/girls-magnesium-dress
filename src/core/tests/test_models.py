# -*- coding: utf-8 -*-
import re

from core.models import Survey, User
from core.tests.mocks import generate_surveys
from djangae.test import TestCase
from django.test import override_settings
from core.tests.mommy_recepies import make_user


class SurveyTest(TestCase):
    """Test case for `core.Survey` model."""

    def setUp(self):
        self.surveys = generate_surveys()

    def test_uid_is_generated_on_save(self):
        """Test that the survey generates a sid on save."""
        s = Survey(company_name="test", country="IT", industry="re")
        self.assertFalse(s.sid)
        s.save()
        self.assertTrue(s.sid)
        self.surveys = generate_surveys()

    def test_link(self):
        """
        Test that the link has the sid set
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], survey.sid)

    def test_sponsor_link(self):
        """
        Test that the sponsor link has both the sid and sponsor flag
        in the query string,
        """
        survey = self.surveys[0]
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
        survey = Survey.objects.create(industry='IT')
        self.assertEqual(survey.industry, 'IT')

    def test_company_name_unicode(self):
        """Test that company name can have unicode characters."""
        unicode_company_name = u"Company name unicode Æ"
        s = Survey(company_name=unicode_company_name, country="IT", industry="re")
        s.save()
        self.assertTrue(s.sid)
        survey = Survey.objects.get(sid=s.sid)
        self.assertEqual(unicode_company_name, survey.company_name)


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
        self.assertFalse(stored_user.is_whitelisted)

    @override_settings(
        WHITELISTED_USERS=[
            'whitelisted@gmail.com',
        ]
    )
    def test_regular_user_whiltelisted(self):
        email = "user@gmail.com"
        whitelisted_email = "whitelisted@gmail.com"
        email_hashed = "cba1f2d695a5ca39ee6f343297a761a4"
        make_user(email=email)
        make_user(email=whitelisted_email)

        self.assertEqual(User.objects.count(), 2)

        stored_user = User.objects.get(email=email)
        stored_user_whitelisted = User.objects.get(email=whitelisted_email)

        self.assertEqual(stored_user.engagement_lead, email_hashed)
        self.assertEqual(stored_user.email, email)
        self.assertFalse(stored_user.is_whitelisted)

        self.assertEqual(stored_user_whitelisted.email, whitelisted_email)
        self.assertTrue(stored_user_whitelisted.is_whitelisted)
