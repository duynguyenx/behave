from features.pageobjects.page import Page
from features.pageobjects.login import constants


class LoginPage(Page):
    def input_username(self, username):
        self.type_text(constants.LOG_IN['USERNAME_INPUTBOX'], username)

    def input_password(self, password):
        self.type_text(constants.LOG_IN['PASSWORD_INPUTBOX'], password)
