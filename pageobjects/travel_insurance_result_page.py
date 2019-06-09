from pageobjects.page import Page
from pageobjects import constants


class TravelInsuranceResultPage(Page):
    def get_all_card_brand_names(self):
        return self.get_text_of_elements(constants.TRAVEL_INSURANCE_RESULT_PAGE['ALL_CARD_BRAND_NAMES'])

    def get_filter_overview_values(self):
        return self.get_element_text(constants.TRAVEL_INSURANCE_RESULT_PAGE['FILTER_VALUES'])
