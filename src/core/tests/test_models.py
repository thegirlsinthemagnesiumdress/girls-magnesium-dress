import re

from core.models import Survey
from core.tests.mocks import generate_surveys
from djangae.test import TestCase


class SurveyTest(TestCase):
    """Test case for `core.Survey` model."""

    def setUp(self):
        self.surveys = generate_surveys()

    def test_uid_is_generated_on_save(self):
        """Test that the survey generates a sid on save."""
        s = Survey(company_name="1")
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
