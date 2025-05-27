import base64
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

class GmailIntegrator:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"], scopes=SCOPES)
        self.service = build("gmail", "v1", credentials=creds)

    def list_unread(self, max_results=5):
        results = self.service.users().messages().list(
            userId="me", q="is:unread", maxResults=max_results).execute()
        msgs = results.get("messages", [])
        threads = []
        for m in msgs:
            thread = self.service.users().messages().get(
                userId="me", id=m["id"], format="full").execute()
            threads.append(thread)
        return threads

    def send_email(self, to, subject, body_text):
        message = ("From: me\r\nTo: {}\r\nSubject: {}\r\n\r\n{}"
                   .format(to, subject, body_text))
        raw = base64.urlsafe_b64encode(message.encode()).decode()
        return self.service.users().messages().send(
            userId="me", body={"raw": raw}).execute()
