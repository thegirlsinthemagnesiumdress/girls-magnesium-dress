"""Handles interacting with the Google Sheets API."""
from google.appengine.api import memcache, urlfetch

import httplib2
from apiclient import discovery
from oauth2client.contrib.appengine import AppAssertionCredentials


_SHEETS_SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
_DRIVE_SCOPE = 'https://www.googleapis.com/auth/drive'
WRITER_ROLE = 'writer'


def sheets_api_factory(scope=_SHEETS_SCOPE):
    """Builds a Sheets API client."""
    urlfetch.set_default_fetch_deadline(60)
    credentials = AppAssertionCredentials(scope)
    http = credentials.authorize(httplib2.Http(memcache))
    return discovery.build('sheets', 'v4', http=http)


def drive_api_factory(scope=_DRIVE_SCOPE):
    """Builds a Drive API client."""
    urlfetch.set_default_fetch_deadline(60)
    credentials = AppAssertionCredentials(scope)
    http = credentials.authorize(httplib2.Http(memcache))
    return discovery.build('drive', 'v3', http=http)


def export_data(title, headers, rows, share_with):
    sheets_api = sheets_api_factory()
    spreadsheet = {
        'properties': {
            'title': title
        }
    }
    spreadsheet = sheets_api.spreadsheets().create(body=spreadsheet).execute()
    sheet = _clear_sheets_and_create_new_one(spreadsheet)
    _write_headers_to_sheet(spreadsheet, sheet, headers)
    _write_rows_to_sheet(spreadsheet, sheet, rows)
    _share_with(spreadsheet, share_with)

    return spreadsheet['spreadsheetUrl']


def _clear_sheets_and_create_new_one(spreadsheet):
    sheets_api = sheets_api_factory()
    existing_sheet_ids = (s['properties']['sheetId'] for s in spreadsheet['sheets'])

    requests = []
    requests.extend(
        [{'addSheet': {'properties': {'hidden': False}}}]
    )
    requests.extend(
        [{'deleteSheet': {'sheetId': sheet_id}} for sheet_id in existing_sheet_ids]
    )

    body = {'requests': requests}

    response = sheets_api.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet['spreadsheetId'], body=body
    ).execute()

    sheet = response['replies'][0]['addSheet']['properties']

    return sheet


def _write_headers_to_sheet(spreadsheet, sheet, headers):
    sheets_api = sheets_api_factory()

    body = {'values': [headers]}

    sheets_api.spreadsheets().values().append(
        spreadsheetId=spreadsheet['spreadsheetId'],
        range=sheet['title'],
        body=body,
        valueInputOption='RAW',
    ).execute()


def _write_rows_to_sheet(spreadsheet, sheet, rows):
    sheets_api = sheets_api_factory()

    body = {'values': rows}

    sheets_api.spreadsheets().values().append(
        spreadsheetId=spreadsheet['spreadsheetId'],
        range=sheet['title'],
        body=body,
        valueInputOption='RAW',
    ).execute()


def _share_with(spreadsheet, email):
    drive_api = drive_api_factory()
    drive_api.permissions().create(
        fileId=spreadsheet['spreadsheetId'],
        sendNotificationEmail=True,
        body={
            "type": "user",
            "emailAddress": email,
            "role": WRITER_ROLE,
        }
    ).execute()
