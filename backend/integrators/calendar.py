from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

class CalendarIntegrator:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"], scopes=SCOPES)
        self.service = build("calendar", "v3", credentials=creds)

    def list_events(self, calendar_id='primary', time_min=None, time_max=None):
        events = (self.service.events().list(
            calendarId=calendar_id, timeMin=time_min, timeMax=time_max,
            singleEvents=True, orderBy='startTime').execute().get('items', []))
        return events
