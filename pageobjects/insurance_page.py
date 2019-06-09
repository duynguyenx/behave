from pageobjects.page import Page
from pageobjects import constants


class InsurancePage(Page):
    def click_travel_tab(self):
        self.click_element(constants.INSURANCE_PAGE['TRAVEL_TAB'])
