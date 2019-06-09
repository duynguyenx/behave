from pageobjects.page import Page
from pageobjects import constants


class HomePage(Page):
    def click_insurance_tab(self):
        self.click_element(constants.HOME_PAGE['INSURANCE_TAB'])
