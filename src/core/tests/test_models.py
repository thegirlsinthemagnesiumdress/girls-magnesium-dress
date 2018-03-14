from djangae.test import TestCase
from core.models import Survey, User
from core.tests.mocks import generate_surveys

import re

class UserTest(TestCase):
    def test_is_qualtrics_false_by_default(self):
        user = User.objects.create(
            username='test1',
            email='test@test.com',
            password='pass',
        )
        self.assertFalse(user.is_qualtrics)

class SurveyTest(TestCase):
    def setUp(self):
        self.surveys = generate_surveys()

    def test_uid_is_generated_on_save(self):
        """
        Test that the survey generates a uid on save.
        """
        s = Survey(company_name="1")
        self.assertFalse(s.uid)
        s.save()
        self.assertTrue(s.uid)
        self.surveys = generate_surveys()

    def test_link(self):
        """
        Test that the link has the uid set
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link)
        self.assertEqual(match.groups(1)[0], survey.uid)


    def test_sponsor_link(self):
        """
        Test that the sponsor link has both the uid and sponsor flag
        in the query string,
        """
        survey = self.surveys[0]
        match = re.search(r'sid=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], survey.uid)
        match = re.search(r'sp=([^&]*)', survey.link_sponsor)
        self.assertEqual(match.groups(1)[0], 'true')
