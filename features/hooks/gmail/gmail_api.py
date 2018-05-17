from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from conf import constants


class GmailAPI(object):

    # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
    SCOPES = 'https://mail.google.com/'

    # Path to the client_secret.json file downloaded from the Developer Console
    CLIENT_SECRET_FILE = './conf/gmail_client_secret.json'

    # Application name set in Google Developers Console https://console.developers.google.com/apis/credentials)
    APPLICATION_NAME = 'UI Behave Test'

    def __init__(self):
        # Authorize the httplib2.Http object with our credentials
        self.service = GmailAPI.create_service()

    @staticmethod
    def create_service():

        # Location of the credentials storage file
        store = file.Storage('./features/hooks/gmail/gmail.storage.json')

        # Try to retrieve credentials from storage or run the flow to generate them
        credentials = store.get()
        if not credentials or credentials.invalid:
            # Start the OAuth flow to retrieve credentials
            flow = client.flow_from_clientsecrets(GmailAPI.CLIENT_SECRET_FILE, GmailAPI.SCOPES)
            flow.user_agent = GmailAPI.APPLICATION_NAME
            credentials = tools.run_flow(flow, store, flags=None)

        # Build the Gmail service from discovery
        return build(serviceName=constants.GMAIL_API['service_name'], version=constants.GMAIL_API['version'],
                     http=credentials.authorize(Http()))

    def get_mail_list(self, user='me', query=None):
        # Get and Return the email list based on provided query
        # Check https://support.google.com/mail/answer/7190?hl=en for available queries
        return self.service.users().messages().list(userId=user, q=query).execute()

    def get_mail_content(self, user='me', msg_id=None):
        # Get and Return email content from email id (msg_id)
        return self.service.users().messages().get(userId=user, id=msg_id).execute()

    def delete_email(self, user='me', msg_id=None):
        # Hard Delete email id (msg_id)
        self.service.users().messages().delete(userId=user, id=msg_id).execute()

    def mark_email_as_read(self, user='me', msg_id=None):
        self.service.users().messages().modify(userId=user, id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
