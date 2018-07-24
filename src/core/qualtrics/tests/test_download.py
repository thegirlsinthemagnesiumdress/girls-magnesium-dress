import io
import json
import StringIO
import zipfile

import mock

from core.qualtrics import download, exceptions
from core.tests.mocks import qualtrics_export
from djangae.test import TestCase


export_generation_response = {
    'meta': {
        'httpStatus': '200 - OK',
        'requestId': 'ca35bacf-3fc4-4b75-ac10-7893be8d8a00'
    },
    'result': {
        'id': 'ES_tfj9degejed7c5qom0ulq7eehu'
    }
}


progress_generation_response = {
    'meta': {
        'httpStatus': '200 - OK',
        'requestId': '6d44e2da-dfa1-4590-adca-a9a814d5bd0c'
    },
    'result': {
        'status': 'complete',
        'percentComplete': 100.0,
        'file': 'https://somedomain.com/ES_tfj9degejed7c5qom0ulq7eehu/file'
    }
}

error_response = {
    'meta': {
        'httpStatus': '404 - Not Found',
        'error': {
            'errorMessage': 'Export id not found.',
            'errorCode': 'EPPH_4'
        },
        'requestId': '2a8ca6f7-9339-4352-b8ca-9f09840ba90e'
    }
}


def get_zipped_content(num_files=1):
    in_memory_zip = StringIO.StringIO()
    zf = zipfile.ZipFile(in_memory_zip, 'w')
    for i in range(num_files):
        zf.writestr('results_{}.json'.format(i), json.dumps(qualtrics_export))
    zf.close()
    return in_memory_zip.getvalue()


class MockResponse(object):
    """Mock `google.appengine.api.urlfetch.fetch` response."""
    def __init__(self, content, zipped=False):
        if zipped:
            self.content = content
        else:
            self.content = json.dumps(content)

        self.status_code = 200
        self.headers = {}


class FetchResultsTest(TestCase):
    """Test case for `core.qualtrics.download.fetch_results` function."""

    def setUp(self):
        self.mocks = [
            MockResponse(export_generation_response),
            MockResponse(progress_generation_response),
            MockResponse(get_zipped_content(), zipped=True)
        ]

    @mock.patch('google.appengine.api.urlfetch.fetch')
    def test_fetch_results_correctly(self, mock_request):
        """When export is generated correctly."""
        mock_request.side_effect = self.mocks

        download.fetch_results()

        mock_request.assert_called()
        self.assertEqual(mock_request.call_count, 3)

    @mock.patch('google.appengine.api.urlfetch.fetch')
    def test_fetch_results_generate_export_fails(self, mock_request):
        """When the first step, creating data export, fails."""
        self.mocks[0] = MockResponse(error_response)
        mock_request.side_effect = self.mocks

        self.assertRaises(exceptions.FetchResultException, download.fetch_results)
        mock_request.assert_called()
        self.assertEqual(mock_request.call_count, 1)

    @mock.patch('google.appengine.api.urlfetch.fetch')
    def test_fetch_results_check_export_progress_fails(self, mock_request):
        """When the second step, check export creation progress, fails."""
        self.mocks[1] = MockResponse(error_response)
        mock_request.side_effect = self.mocks

        self.assertRaises(exceptions.FetchResultException, download.fetch_results)
        mock_request.assert_called()
        self.assertEqual(mock_request.call_count, 2)

    @mock.patch('google.appengine.api.urlfetch.fetch')
    def test_fetch_results_get_exported_data_fails(self, mock_request):
        """When the third step, get export zip file, fails."""
        self.mocks[2] = MockResponse(error_response)
        mock_request.side_effect = self.mocks

        self.assertRaises(exceptions.FetchResultException, download.fetch_results)
        mock_request.assert_called()
        self.assertEqual(mock_request.call_count, 3)


class UnpackZipTest(TestCase):
    """Test case for `core.qualtrics.download._unpack_zip` function."""

    def test__unpack_zip_single_file(self):
        """When unzip an archive with a single file."""
        with io.BytesIO() as in_memory_buffer:
            in_memory_buffer.write(get_zipped_content())
            files_in_memory = [file_content for file_content in download._unpack_zip(in_memory_buffer)]
        self.assertEqual(len(files_in_memory), 1)

    def test__unpack_zip_multiple_files(self):
        """When unzip an archive with a multiple files."""
        with io.BytesIO() as in_memory_buffer:
            in_memory_buffer.write(get_zipped_content(num_files=5))
            files_in_memory = [file_content for file_content in download._unpack_zip(in_memory_buffer)]
        self.assertEqual(len(files_in_memory), 5)

    def test__unpack_zip_empty_archive(self):
        """When unzip an archive with no files."""
        with io.BytesIO() as in_memory_buffer:
            in_memory_buffer.write(get_zipped_content(num_files=0))
            files_in_memory = [file_content for file_content in download._unpack_zip(in_memory_buffer)]
        self.assertEqual(len(files_in_memory), 0)
