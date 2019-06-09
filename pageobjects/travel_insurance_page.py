from pageobjects.page import Page
from pageobjects import constants


class TravelInsurancePage(Page):

    def click_and_select_policy_dropdown(self, policy_name):
        self.click_and_select_option_from_dropdown(constants.TRAVEL_INSURANCE_PAGE['POLICY_TYPE_DROPDOWN'], policy_name)

    def click_and_select_whos_going_dropdown(self, option_name):
        self.click_and_select_option_from_dropdown(constants.TRAVEL_INSURANCE_PAGE['WHO_GOING_DROPDOWN'], option_name)

    def click_and_select_destination_dropdown(self, option_name):
        self.click_and_select_option_from_dropdown(constants.TRAVEL_INSURANCE_PAGE['DESTINATION_DROPDOWN'], option_name)

    def click_and_select_start_date(self, date):
        self.click_element(constants.TRAVEL_INSURANCE_PAGE['START_DATE'])
        self.select_date_on_date_picker(date)

    def click_and_select_end_date(self, date):
        self.click_element(constants.TRAVEL_INSURANCE_PAGE['END_DATE'])
        self.select_date_on_date_picker(date)

    def click_show_result_button(self):
        self.click_element(constants.TRAVEL_INSURANCE_PAGE['SHOW_RESULT_BUTTON'])
