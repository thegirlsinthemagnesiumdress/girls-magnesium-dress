from djangae.test import TestCase
from core.models import Survey
from core.tests.mocks import generate_surveys

import re

class SurveyTest(TestCase):
    def test_uid_is_generated_on_save(self):
        s = Survey(company_name="1")
        self.assertFalse(s.uid)
        s.save()
        self.assertTrue(s.uid)

