from pageobjects.core import BasePage
from pageobjects.core.elements import Element
from pageobjects.core.enums import WaitType
from pageobjects.locators import travel_insurance_result_page_locators as locators


class TravelInsuranceResultPage(BasePage):
    def get_all_card_brand_names(self):
        elements = self.wait_elements(locators.ALL_CARD_BRAND_NAMES, WaitType.WAIT_FOR_ELEMENTS_TO_BE_PRESENTED)
        return [element.text for element in elements]

    def get_filter_overview_values(self):
        return Element(locators.FILTER_VALUES, self.driver).get_text()

