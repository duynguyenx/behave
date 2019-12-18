from pageobjects.core import BasePage
from pageobjects.core.elements import Element
from pageobjects.locators import home_page_locators


class HomePage(BasePage):
    def click_insurance_tab(self):
        Element(home_page_locators.TABS['INSURANCE_TAB'], self.driver).click()

