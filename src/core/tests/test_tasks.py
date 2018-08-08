import mock

from core.models import Survey, SurveyResult
from core.tasks import get_results, send_emails_for_new_reports, is_valid_email, _create_survey_result
from djangae.test import TestCase
from mocks import get_mocked_results
from mommy_recepies import make_survey, make_survey_result
from core.qualtrics.exceptions import FetchResultException
from django.shortcuts import reverse


class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results())
    def test_new_survey_first_time_download(self, download_mock):
        """We're assuming that all the Surveys have been created previously."""
        make_survey(sid='1')
        make_survey(sid='2')
        make_survey(sid='3')

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results())
    def test_surveys_results_are_always_saved(self, download_mock):
        """Survey results are saved anyway, regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        get_results()

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results(response_id='AAB'))
    def test_partial_download_existing_survey(self, download_mock):
        # survey has been created on datastore
        survey = make_survey(sid='1')
        make_survey(sid='2')
        make_survey(sid='3')

        # only survey result with response_id='AAB' has been downloaded
        make_survey_result(survey=survey, response_id='AAB')

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 1)

        get_results()

        # no new Survey objects are created
        self.assertEqual(Survey.objects.count(), 3)
        # mock is called with response_id
        download_mock.assert_called_once_with(response_id='AAB')
        # only two new items will be created
        self.assertEqual(SurveyResult.objects.count(), 3)

    @mock.patch('core.qualtrics.download.fetch_results')
    def test_fetch_results_fails(self, download_mock):
        exception_body = {
            'meta': {
                'httpStatus': 400,
                'error': {
                    'errorMesasge': 'some error'
                }
            }
        }
        download_mock.side_effect = FetchResultException(exception_body)

        survey = make_survey(sid='1')
        make_survey_result(survey=survey, response_id='AAB')
        self.assertEqual(SurveyResult.objects.count(), 1)

        with mock.patch('core.tasks._create_survey_result') as survey_result_mock:
            get_results()
            survey_result_mock.assert_not_called()
            download_mock.assert_called_once_with(response_id='AAB')
            self.assertEqual(Survey.objects.count(), 1)
            self.assertEqual(SurveyResult.objects.count(), 1)


class EmailValidatorTestCase(TestCase):
    """Tests for is_valid_email function."""

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email(None))
        self.assertFalse(is_valid_email(''))
        self.assertFalse(is_valid_email('astring'))
        self.assertFalse(is_valid_email('email@example.com\n'))
        self.assertFalse(is_valid_email('email@example'))
        self.assertFalse(is_valid_email('email\n@example.com'))
        self.assertFalse(is_valid_email('email@example\n.com'))

    def test_valid_emails(self):
        self.assertTrue(is_valid_email('email@example.com'))
        self.assertTrue(is_valid_email('email123@example.com'))


class CreateSurveyResultTestCase(TestCase):
    """Tests for send_mail_report function."""
    def setUp(self):
        self.responses = get_mocked_results().get('responses')

    def test_survey_result_created(self):
        """`SurveyResult` is always created."""
        make_survey(sid=1)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _create_survey_result(self.responses[:1])

        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 1)

    def test_survey_result_created_no_survey_found(self):
        """When a Survey is not found, `SurveyResult` is created anyway."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _create_survey_result(self.responses[:1])

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 1)


class SendEmailTestCase(TestCase):
    """Tests for send_emails_for_new_reports function."""
    def setUp(self):
        self.responses = get_mocked_results().get('responses')

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_email_not_send_to_invalid(self, email_mock):
        """`SurveyResult` email is not sent, because `to` field is invalid."""
        email_list = [
            ('invalidemail', 'test@example.com', '1')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_not_called()

        # if 'to' is not set, then don't send email
        email_list = [
            (None, 'test@example.com', '1')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_not_called()

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_email_is_correctly_sent_bcc_invalid(self, email_mock):
        """`SurveyResult` email is sent to `to` recipient, but not to `bbc` because `bcc` field is invalid."""
        email_list = [
            ('test@example.com', 'invalidemail', '1')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_called()

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_email_is_correctly_sent_with_bcc(self, email_mock):
        """`SurveyResult` email is sent correctly."""
        email_list = [
            ('test@example.com', 'test@example.com', '1')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_called()

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_email_is_correctly_sent_no_bcc(self, email_mock):
        """`SurveyResult` email is sent to `to` recipient, but not to `bbc` because `bcc` field is invalid."""
        email_list = [
            ('test@example.com', None, '1')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_called()

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_email_is_correctly_sent_multiple_emails(self, email_mock):
        """`SurveyResult` email is sent correctly, when email_list has more than one element."""
        email_list = [
            ('test@example.com', 'test@example.com', '1'),
            ('test2@example.com', 'test3@example.com', '2')
        ]

        send_emails_for_new_reports(email_list)
        email_mock.assert_called()
        self.assertEqual(email_mock.call_count, 2)
