from pageobjects.base_page import BasePage
from pageobjects.elements import BaseElement
from pageobjects import constants


class TravelInsuranceResultPage(BasePage):
    def get_all_card_brand_names(self):
        elements = self.driver.wait_for_elements_to_be_presented(
            constants.TRAVEL_INSURANCE_RESULT_PAGE['ALL_CARD_BRAND_NAMES'])
        return [element.text for element in elements]

    def get_filter_overview_values(self):
        element = BaseElement(constants.TRAVEL_INSURANCE_RESULT_PAGE['FILTER_VALUES'], self.driver)
        return element.get_text()
