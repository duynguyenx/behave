from pageobjects.core import BasePage
from pageobjects.core.elements import Element
from pageobjects.locators import insurance_page_locators


class InsurancePage(BasePage):
    def click_travel_tab(self):
        Element(insurance_page_locators.TABS['TRAVEL_TAB'], self.driver).click()
