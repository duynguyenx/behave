from pageobjects.base_page import BasePage
from pageobjects.elements import BaseElement
from pageobjects import constants


class InsurancePage(BasePage):
    def click_travel_tab(self):
        travel_tab_locator = constants.INSURANCE_PAGE['TRAVEL_TAB']
        travel_element = BaseElement(travel_tab_locator, self.driver)
        travel_element.click()
