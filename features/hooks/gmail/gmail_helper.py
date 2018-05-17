from features.hooks.gmail.gmail_api import GmailAPI
import base64
import time
from datetime import datetime, timedelta
from conf import constants
from features.hooks.gmail.mail import Mail


class GmailHelper(GmailAPI):

    CHECK_MAIL_TIMEOUT = 15
    CHECK_MAIL_POLL = 0.5

    def fetch_mails(self, query, timeout=CHECK_MAIL_TIMEOUT, poll=CHECK_MAIL_POLL):
        email_data = {}
        end_time = datetime.now() + timedelta(seconds=timeout)
        while True:
            email_data = self.get_mail_list(query=query)
            if email_data['resultSizeEstimate']:
                break
            if datetime.now() > end_time:
                raise LookupError(constants.RAISING_ERRORS['EMAIL_TIME_OUT'])
            time.sleep(poll)

        mail_list = []
        for msg in email_data['messages']:
            message = self.decode_mail_body(msg_id=msg['id'])
            mail = Mail(msg['id'], message)
            mail_list.append(mail)
        return mail_list

    def get_new_mails(self, mail_address='me', mark_email_as_read=True,
                      timeout=CHECK_MAIL_TIMEOUT, poll=CHECK_MAIL_POLL):
        query = 'is:unread to:{}'.format(mail_address)
        mail_list = self.fetch_mails(query=query, timeout=timeout, poll=poll)
        if mark_email_as_read:
            for mail in mail_list:
                self.mark_email_as_read(msg_id=mail['id'])
        return mail_list

    def decode_mail_body(self, user='me', msg_id=None):
        msg_content = self.get_mail_content(user=user, msg_id=msg_id)
        return base64.urlsafe_b64decode(msg_content['payload']['body']['data'].encode('ASCII'))
