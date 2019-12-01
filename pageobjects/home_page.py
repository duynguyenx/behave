from pageobjects.base_page import BasePage
from pageobjects.elements import BaseElement
from pageobjects import constants


class HomePage(BasePage):
    def click_insurance_tab(self):
        insurance_locator = constants.HOME_PAGE['INSURANCE_TAB']
        insurance_element = BaseElement(insurance_locator, self._driver)
        insurance_element.click()

