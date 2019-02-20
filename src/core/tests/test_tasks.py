# encoding=utf-8
import mock

from core.models import Survey, SurveyResult, SurveyDefinition
from core.tasks import _get_results, send_emails_for_new_reports, is_valid_email, _create_survey_results, generate_csv_export, _update_responses_with_text, _get_definition, sync_qualtrics
from djangae.test import TestCase
from mocks import get_mocked_results, MOCKED_DIMENSIONS, get_mocked_results_unfished, get_survey_definition, MOCKED_TENANTS
from mommy_recepies import make_survey, make_survey_result, make_survey_definition
from core.qualtrics.exceptions import FetchResultException
from django.test import override_settings
from django.utils import dateparse
from django.utils.timezone import make_aware
import pytz
from collections import OrderedDict


@override_settings(
    DIMENSIONS=MOCKED_DIMENSIONS,
    TENANTS=MOCKED_TENANTS,
)
class sync_qualtricsTestCase(TestCase):
    """
    Returns `True` if the user is set in the admin console and is a googler
    `False` otherwise.
    """
    @mock.patch('core.tasks._get_definition', return_value='something')
    @mock.patch('core.tasks._get_results', return_value='something')
    def test_syncs_def_and_results(self, get_result_mock, get_survey_definition_mock):
        sync_qualtrics()
        self.assertEqual(get_survey_definition_mock.call_count, 1)

        all_calls = get_survey_definition_mock.call_args_list

        args, kwargs = all_calls[0]
        self.assertEqual(len(args), 1)
        self.assertIsNotNone(args[0])

        self.assertEqual(get_result_mock.call_count, 1)

        all_calls = get_result_mock.call_args_list

        args, kwargs = all_calls[0]
        self.assertEqual(len(args), 2)
        self.assertIsNotNone(args[0])

    @mock.patch('core.tasks._get_definition', return_value=None)
    @mock.patch('core.tasks._get_results', return_value='something')
    def test_syncs_def_fails(self, get_result_mock, get_survey_definition_mock):
        sync_qualtrics()
        self.assertEqual(get_survey_definition_mock.call_count, 1)
        self.assertEqual(get_result_mock.call_count, 0)


@override_settings(
    DIMENSIONS=MOCKED_DIMENSIONS
)
class GetResultsTestCase(TestCase):
    """Tests for get_result function"""

    def setUp(self):
        self.tenant = MOCKED_TENANTS['tenant1']

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch(
        'core.qualtrics.download.fetch_results',
        side_effect=[get_mocked_results(), get_mocked_results(text=True)]
    )
    def test_new_survey_first_time_download(self, download_mock, send_email_mock):
        """Test surveys are downloaded for the first time.

        We're assuming that all the Surveys have been created previously and
        SurveyResults are created only if the survey has been completed (`Finished`
        flag set to `1`).
        """
        make_survey()
        make_survey()
        make_survey()

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _get_results(self.tenant, make_survey_definition())

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 3)

        self.assertTrue(download_mock.called)
        self.assertEqual(download_mock.call_count, 2)
        all_calls = download_mock.call_args_list
        # first call to get all results it should have started_after = None
        args, kwargs = all_calls[0]
        self.assertIsNone(kwargs.get('started_after'))
        # second call to get all text results it should have started_after = None and text `True`
        args, kwargs = all_calls[1]
        self.assertIsNone(kwargs.get('started_after'))
        self.assertEqual(kwargs.get('text'), True)

        self.assertTrue(send_email_mock.called)
        args, kwargs = send_email_mock.call_args
        self.assertEqual(len(args[0]), 3)

    @override_settings(
        INDUSTRIES={
            'IT': 'IT',
            'B': 'B',
        }
    )
    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch(
        'core.qualtrics.download.fetch_results',
        side_effect=[get_mocked_results(), get_mocked_results(text=True)]
    )
    def test_surveys_results_and_survey_updated(self, download_mock, send_email_mock):
        """Survey results are saved anyway (if survey has been completed), regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        survey = make_survey(sid=1)
        make_survey()
        make_survey()

        _get_results(self.tenant, make_survey_definition())

        survey_1 = Survey.objects.get(pk=survey.sid)

        # Last result is updated.
        self.assertIsNotNone(survey_1.last_survey_result)

        self.assertTrue(download_mock.called)
        self.assertEqual(download_mock.call_count, 2)
        all_calls = download_mock.call_args_list
        # first call to get all results it should have started_after = None
        args, kwargs = all_calls[0]
        self.assertIsNone(kwargs.get('started_after'))
        # second call to get all text results it should have started_after = None and text `True`
        args, kwargs = all_calls[1]
        self.assertIsNone(kwargs.get('started_after'))
        self.assertEqual(kwargs.get('text'), True)

        # send_emails_for_new_reports is called
        self.assertTrue(send_email_mock.called)
        args, kwargs = send_email_mock.call_args
        self.assertEqual(len(args[0]), 3)

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch(
        'core.qualtrics.download.fetch_results',
        side_effect=[get_mocked_results(), get_mocked_results(text=True)]
    )
    def test_surveys_results_are_always_saved(self, download_mock, send_email_mock):
        """Survey results are saved anyway (if survey has been completed), regardless Survey's related object exists."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _get_results(self.tenant, make_survey_definition())

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)

        # send_emails_for_new_reports is called
        self.assertTrue(send_email_mock.called)
        args, kwargs = send_email_mock.call_args
        self.assertEqual(len(args[0]), 3)

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch(
        'core.qualtrics.download.fetch_results',
        side_effect=[
            get_mocked_results(started_after=dateparse.parse_datetime('2018-07-31 14:16:06')),
            get_mocked_results(started_after=dateparse.parse_datetime('2018-07-31 14:16:06'), text=True)]
    )
    def test_partial_download_existing_survey(self, download_mock, send_email_mock):
        # survey has been created on datastore
        survey = make_survey()
        make_survey()
        make_survey()

        # only survey result with date after 2018-07-31 14:16:06 has been downloaded
        string_survey_started_at = '2018-07-31 14:16:06'
        survey_started_at = make_aware(dateparse.parse_datetime(string_survey_started_at), pytz.timezone('US/Mountain'))
        make_survey_result(survey=survey, started_at=string_survey_started_at)

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 1)

        _get_results(self.tenant, make_survey_definition())

        # no new Survey objects are created
        self.assertEqual(Survey.objects.count(), 3)

        self.assertEqual(download_mock.call_count, 2)
        all_calls = download_mock.call_args_list
        # first call to get all results it should have started_after = None
        args, kwargs = all_calls[0]
        self.assertIsNotNone(kwargs.get('started_after'))
        self.assertEqual(kwargs.get('started_after'), survey_started_at)
        # second call to get all text results it should have started_after = None and text `True`
        args, kwargs = all_calls[1]
        self.assertIsNotNone(kwargs.get('started_after'))
        self.assertEqual(kwargs.get('started_after'), survey_started_at)
        self.assertEqual(kwargs.get('text'), True)

        # only two new items will be created
        self.assertEqual(SurveyResult.objects.count(), 3)

        # send_emails_for_new_reports is called
        self.assertTrue(send_email_mock.called)
        args, kwargs = send_email_mock.call_args
        self.assertEqual(len(args[0]), 2)

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch('core.qualtrics.download.fetch_results')
    def test_fetch_results_fails(self, download_mock, send_email_mock):
        exception_body = {
            'meta': {
                'httpStatus': 400,
                'error': {
                    'errorMesasge': 'some error'
                }
            }
        }
        download_mock.side_effect = FetchResultException(exception_body)

        string_survey_started_at = '2018-07-31 14:16:06'
        survey_started_at = make_aware(dateparse.parse_datetime(string_survey_started_at), pytz.timezone('US/Mountain'))
        survey = make_survey()
        make_survey_result(survey=survey, started_at=string_survey_started_at)
        self.assertEqual(SurveyResult.objects.count(), 1)

        with mock.patch('core.tasks._create_survey_results') as survey_result_mock:
            _get_results(self.tenant, make_survey_definition())
            survey_result_mock.assert_not_called()
            download_mock.assert_called_once_with(self.tenant['QUALTRICS_SURVEY_ID'], started_after=survey_started_at)
            self.assertEqual(Survey.objects.count(), 1)
            self.assertEqual(SurveyResult.objects.count(), 1)

            # send_emails_for_new_reports is not called
            self.assertFalse(send_email_mock.called)

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch('core.qualtrics.download.fetch_results', return_value=get_mocked_results_unfished())
    def test_unfinished_surveys_download(self, download_mock, send_email_mock):
        """Test surveys downloaded are unfinished.

        Unfinished surveys should not be saved as Survey, and the email sending
        should not be triggered.
        """
        make_survey()
        make_survey()
        make_survey()

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _get_results(self.tenant, make_survey_definition())

        self.assertEqual(Survey.objects.count(), 3)
        self.assertEqual(SurveyResult.objects.count(), 0)

        # send_emails_for_new_reports is not called
        self.assertFalse(send_email_mock.called)

    @mock.patch('core.tasks.send_emails_for_new_reports')
    @mock.patch(
        'core.qualtrics.download.fetch_results',
        side_effect=[get_mocked_results(), get_mocked_results(text=True)]
    )
    def test_new_fetch_results_is_called_with_survey_id(self, download_mock, send_email_mock):
        """Test fetch_results is always called with survey_id as positional paramenter."""
        make_survey()
        make_survey()
        make_survey()

        _get_results(self.tenant, make_survey_definition())

        self.assertTrue(download_mock.called)
        self.assertEqual(download_mock.call_count, 2)
        all_calls = download_mock.call_args_list
        # first call to get all results it should have started_after = None
        args, kwargs = all_calls[0]

        self.assertIsNone(kwargs.get('started_after'))
        self.assertEqual(len(args), 1)
        self.assertIsNotNone(args[0])
        # second call to get all text results it should have started_after = None and text `True`
        args, kwargs = all_calls[1]
        self.assertIsNone(kwargs.get('started_after'))
        self.assertEqual(len(args), 1)
        self.assertIsNotNone(args[0])
        self.assertEqual(kwargs.get('text'), True)

        self.assertTrue(send_email_mock.called)
        args, kwargs = send_email_mock.call_args
        self.assertEqual(len(args[0]), 3)


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


@override_settings(
    DIMENSIONS=MOCKED_DIMENSIONS
)
class CreateSurveyResultTestCase(TestCase):
    """Tests for _create_survey_results function, when survey has been completed."""
    def setUp(self):
        responses_values = get_mocked_results().get('responses')
        responses_text = get_mocked_results(text=True).get('responses')
        self.responses = _update_responses_with_text(responses_values, responses_text).values()
        self.response_ids = [response['value'].get('ResponseID') for response in self.responses
                             if response['value'].get('Finished') == '1']
        self.survey_definition = make_survey_definition()

    def test_survey_result_created(self):
        """`SurveyResult` is always created."""
        make_survey()
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 0)

        got_survey_results = _create_survey_results(self.responses, self.survey_definition)
        got_ids = [result.response_id for result in got_survey_results]

        self.assertEqual(Survey.objects.count(), 1)
        # mocked data contains 3 finished survey results
        self.assertEqual(SurveyResult.objects.count(), 3)
        self.assertTrue(isinstance(got_ids, list))
        self.assertTrue(len(got_ids) == len(self.response_ids))
        for response_id in self.response_ids:
            self.assertTrue(response_id in got_ids)

    def test_survey_result_created_no_survey_found(self):
        """When a Survey is not found, `SurveyResult` is created anyway."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        got_survey_results = _create_survey_results(self.responses, self.survey_definition)
        got_ids = [result.response_id for result in got_survey_results]

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)
        self.assertTrue(isinstance(got_ids, list))
        self.assertTrue(len(got_ids) == len(self.response_ids))
        for response_id in self.response_ids:
            self.assertTrue(response_id in got_ids)

    def test_survey_result_not_duplicated(self):
        """When a SurveyResult with a specific response_id already exists, it won't be created again."""
        # presave finished surveys
        for response in self.responses:
            response_value = response['value']
            if response_value.get('Finished') == '1':
                make_survey_result(
                    started_at=response_value.get('StartDate'),
                    response_id=response_value.get('ResponseID'))

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 3)

        got_survey_results = _create_survey_results(self.responses, self.survey_definition)
        got_ids = [result.response_id for result in got_survey_results]

        self.assertEqual(Survey.objects.count(), 0)
        # no new results are created
        self.assertEqual(SurveyResult.objects.count(), 3)
        self.assertTrue(isinstance(got_ids, list))
        self.assertEqual(len(got_ids), 0)


class CreateSurveyResultUnfinishedTestCase(TestCase):
    """Tests for _create_survey_results function, when survey has not been completed."""
    def setUp(self):
        responses_values = get_mocked_results_unfished().get('responses')
        responses_text = get_mocked_results_unfished(text=True).get('responses')
        self.responses = _update_responses_with_text(responses_values, responses_text).values()
        self.survey_definition = make_survey_definition()

    def test_survey_result_created(self):
        """`SurveyResult` is always created."""
        make_survey()
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _create_survey_results(self.responses, self.survey_definition)

        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(SurveyResult.objects.count(), 0)

    def test_survey_result_created_no_survey_found(self):
        """When a Survey is not found, `SurveyResult` is created anyway."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        _create_survey_results(self.responses, self.survey_definition)

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

    def test_survey_result_not_created_for_not_finished_survey(self):
        """When a Survey is not completed, `SurveyResult` is not created."""
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)

        # Asserting we're logging a message if survey is not completed
        with mock.patch('logging.warning') as logging_mock:
            _create_survey_results(self.responses, self.survey_definition)
            self.assertTrue(logging_mock.called)

        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(SurveyResult.objects.count(), 0)


class SendEmailTestCase(TestCase):
    """Tests for send_emails_for_new_reports function."""
    def setUp(self):
        self.responses = get_mocked_results().get('responses')

    @mock.patch('google.appengine.api.mail.EmailMessage.send')
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

    @mock.patch('google.appengine.api.mail.EmailMessage.send')
    def test_email_is_correctly_sent_bcc_invalid(self, email_mock):
        """`SurveyResult` email is sent to `to` recipient, but not to `bbc` because `bcc` field is invalid."""
        email_list = [
            ('test@example.com', 'invalidemail', '1')
        ]

        send_emails_for_new_reports(email_list)
        self.assertEqual(email_mock.call_args_list, [mock.call()])

    @mock.patch('google.appengine.api.mail.EmailMessage.send')
    def test_email_is_correctly_sent_with_bcc(self, email_mock):
        """`SurveyResult` email is sent correctly."""
        email_list = [
            ('test@example.com', 'test@example.com', '1')
        ]

        send_emails_for_new_reports(email_list)
        self.assertEqual(email_mock.call_args_list, [mock.call()])

    @mock.patch('google.appengine.api.mail.EmailMessage.send')
    def test_email_is_correctly_sent_no_bcc(self, email_mock):
        """`SurveyResult` email is sent to `to` recipient, but not to `bbc` because `bcc` field is invalid."""
        email_list = [
            ('test@example.com', None, '1')
        ]

        send_emails_for_new_reports(email_list)
        self.assertEqual(email_mock.call_args_list, [mock.call()])

    @mock.patch('google.appengine.api.mail.EmailMessage.send')
    def test_email_is_correctly_sent_multiple_emails(self, email_mock):
        """`SurveyResult` email is sent correctly, when email_list has more than one element."""
        email_list = [
            ('test@example.com', 'test@example.com', '1'),
            ('test2@example.com', 'test3@example.com', '2')
        ]

        send_emails_for_new_reports(email_list)
        self.assertEqual(email_mock.call_count, 2)


class GenerateExportTestCase(TestCase):

    @mock.patch('cloudstorage.copy2')
    @mock.patch('cloudstorage.open', new_callable=mock.mock_open)
    def test_generate_export_empty(self, cloud_mock, copy_mock):
        generate_csv_export()
        # check mock called the write for writing headers
        handle = cloud_mock()
        handle.write.assert_called_once_with(
            'id,company_name,industry,country,created_at,engagement_lead,dmb,access,audience,attribution,ads,organization,automation\n'
        )

        # check a copy is made
        copy_mock.assert_called_once()

    @mock.patch('cloudstorage.copy2')
    @mock.patch('cloudstorage.open', new_callable=mock.mock_open)
    def test_generate_export_one_survey(self, cloud_mock, copy_mock):
        make_survey()
        generate_csv_export()
        handle = cloud_mock()

        # called once for headers and once for survey
        self.assertEqual(handle.write.call_count, 2)

        # check a copy is made
        copy_mock.assert_called_once()

    @mock.patch('cloudstorage.copy2')
    @mock.patch('cloudstorage.open', new_callable=mock.mock_open)
    def test_generate_export_multi_survey(self, cloud_mock, copy_mock):
        make_survey()
        make_survey()
        generate_csv_export()
        handle = cloud_mock()

        # called once for headers and once for each survey
        self.assertEqual(handle.write.call_count, 3)

    @mock.patch('cloudstorage.copy2')
    @mock.patch('cloudstorage.open', new_callable=mock.mock_open)
    @override_settings(
        COUNTRIES=OrderedDict([
            ('AX', 'Åland Islands'),
        ])
    )
    def test_generate_export_survey_unicode(self, cloud_mock, copy_mock):
        make_survey(company_name=u'ññññññññ')
        make_survey(country='AX')  # unicode country
        generate_csv_export()
        handle = cloud_mock()

        # called once for headers and once for each survey
        self.assertEqual(handle.write.call_count, 3)
        # check a copy is made
        copy_mock.assert_called_once()


class UpdateResponsesWithTextTestCase(TestCase):
    """Tests for _update_responses_with_text function."""

    def test_update_responses_with_text_values_and_text_match(self):
        """When values and text match, all items are merged in the result."""

        responses_values = get_mocked_results().get('responses')
        responses_text = get_mocked_results(text=True).get('responses')

        responses_values_ids = [response.get('ResponseID') for response in responses_values
                                if response.get('Finished') == '1']

        responses_text_ids = [response.get('ResponseID') for response in responses_text
                              if response.get('Finished') == '1']

        responses = _update_responses_with_text(responses_values, responses_text)

        self.assertEqual(len(responses), len(responses_values))
        for val in responses_values_ids:
            self.assertIn(val, responses.keys())

        self.assertEqual(len(responses), len(responses_text))

        for val in responses_text_ids:
            self.assertIn(val, responses)

    def test_update_responses_with_text_more_values_than_text(self):
        """When values has more items than text, result is updated were possible."""

        responses_values = get_mocked_results().get('responses')
        responses_text = get_mocked_results(text=True).get('responses')

        responses_values.append({
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '1',
            'ResponseID': 'BBB',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': '2',
            'Q4': '0',
            'Q5_1': '2',

            'Q5_2': '0',
            'Q5_3': '3',
            'Q6': '4',
            'Q7': '2',

            'Q8': '4',
            'Q10': '0',
            'Q11': '1',
            'Q12': '2',
            'Finished': '1',
        })

        responses_values_ids = [response.get('ResponseID') for response in responses_values
                                if response.get('Finished') == '1']

        responses_text_ids = [response.get('ResponseID') for response in responses_text
                              if response.get('Finished') == '1']

        responses = _update_responses_with_text(responses_values, responses_text)

        self.assertEqual(len(responses), len(responses_values))
        for val in responses_values_ids:
            self.assertIn(val, responses.keys())

        self.assertNotIn('BBB', responses_text_ids)

    def test_update_responses_with_text_more_text_than_values(self):
        """When text has more items than values, text elements not in values should be skipped."""

        responses_values = get_mocked_results().get('responses')
        responses_text = get_mocked_results(text=True).get('responses')

        responses_text.append({
            'Organization-sum': '0.0',
            'Organization-weightedAvg': '0.0',
            'Organization-weightedStdDev': '0.0',
            'sid': '1',
            'ResponseID': 'BBB',
            'Enter Embedded Data Field Name Here...': '',
            'sponsor': '',
            'company_name': 'new survey',
            'dmb': '0.5',
            'StartDate': '2018-07-31 14:16:06',
            'EndDate': '2018-07-31 15:18:56',
            'Q1_1_TEXT': '',
            'Q1_2_TEXT': '',
            'Q2_1_TEXT': '',
            'Q2_2_TEXT': '',

            'Q3': 'Some text for answer Q3',
            'Q4': 'Some text for answer Q4',
            'Q5_1': 'Some text for answer Q5_1',
            'Q5_2': 'Some text for answer Q5_2',
            'Q5_3': 'Some text for answer Q5_3',
            'Q6': 'Some text for answer Q6',
            'Q7': 'Some text for answer Q7',
            'Q8': 'Some text for answer Q8',
            'Q10': 'Some text for answer Q10',
            'Q11': 'Some text for answer Q11',
            'Q12': 'Some text for answer Q12',
            'Finished': '1',
        })

        responses_values_ids = [response.get('ResponseID') for response in responses_values
                                if response.get('Finished') == '1']

        responses = _update_responses_with_text(responses_values, responses_text)

        self.assertEqual(len(responses), len(responses_values))
        for val in responses_values_ids:
            self.assertIn(val, responses.keys())

        self.assertNotIn('BBB', responses.keys())
        self.assertNotIn('BBB', responses_values_ids)


class GetDefinitionTestCase(TestCase):
    """Tests for _get_definition function"""

    def setUp(self):
        self.survey_id = 'surveyid'

    @mock.patch('core.qualtrics.download.fetch_survey', return_value=get_survey_definition())
    def test_new_definition_firts_time(self, download_mock):
        """When there are not survey definition, the first downloaded needs to be stored."""
        self.assertEqual(SurveyDefinition.objects.count(), 0)
        last_definition = _get_definition(self.survey_id)
        self.assertEqual(SurveyDefinition.objects.count(), 1)
        last_stored = SurveyDefinition.objects.latest('last_modified')
        self.assertIsNotNone(last_definition)
        self.assertEqual(last_definition.pk, last_stored.pk)

    @mock.patch('core.qualtrics.download.fetch_survey', return_value=get_survey_definition())
    def test_new_definition_found(self, download_mock):
        """
        When the new downloaded survey definition last modified date is grater than the last stored one,
        it should be saved.
        """

        # create a survey definition way in the past respect to the mock we have
        make_survey_definition(last_modified=dateparse.parse_datetime('2015-11-29T13:27:15Z'))
        self.assertEqual(SurveyDefinition.objects.count(), 1)
        last_definition = _get_definition(self.survey_id)
        # a new definition should be downloaded
        self.assertEqual(SurveyDefinition.objects.count(), 2)
        last_stored = SurveyDefinition.objects.latest('last_modified')
        self.assertIsNotNone(last_definition)
        self.assertEqual(last_definition.pk, last_stored.pk)

    @mock.patch('core.qualtrics.download.fetch_survey', return_value=get_survey_definition())
    def test_new_definition_dont_need_update(self, download_mock):
        """
        When the new downloaded survey definition last modified date is not grater than the last stored one,
        it should not be saved.
        """
        make_survey_definition(last_modified=dateparse.parse_datetime('2019-01-28T16:04:23Z'))
        self.assertEqual(SurveyDefinition.objects.count(), 1)
        last_definition = _get_definition(self.survey_id)
        # a new definition should not be downloaded
        self.assertEqual(SurveyDefinition.objects.count(), 1)
        last_stored = SurveyDefinition.objects.latest('last_modified')
        self.assertIsNotNone(last_definition)
        self.assertEqual(last_definition.pk, last_stored.pk)

    @mock.patch('core.qualtrics.download.fetch_survey')
    def test_definition_download_fails(self, download_mock):
        exception_body = {
            'meta': {
                'httpStatus': 400,
                'error': {
                    'errorMesasge': 'some error'
                }
            }
        }
        download_mock.side_effect = FetchResultException(exception_body)
        with mock.patch('logging.error') as logging_mock:
            last_definition = _get_definition(self.survey_id)
            self.assertIsNone(last_definition)
            self.assertTrue(logging_mock.called)

    @mock.patch('core.qualtrics.download.fetch_survey', return_value=get_survey_definition())
    def test_fetch_survey_called_with_right_parameters(self, download_mock):
        """When fetch_survey is called, check is called with right paramenters."""
        _ = _get_definition(self.survey_id)

        self.assertTrue(download_mock.called)
        self.assertEqual(download_mock.call_count, 1)
        all_calls = download_mock.call_args_list

        args, kwargs = all_calls[0]
        self.assertEqual(len(args), 1)
        self.assertIsNotNone(args[0])
