from pageobjects.page import BasePage, DropdownElement, DatePickerElement, BaseElement
from pageobjects import constants


class TravelInsurancePage(BasePage):

    def click_and_select_policy_dropdown(self, policy_name):
        dropdown_locator = constants.TRAVEL_INSURANCE_PAGE['POLICY_TYPE_DROPDOWN']
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(policy_name, move_to_element=True)

    def click_and_select_whos_going_dropdown(self, option_name):
        dropdown_locator = constants.TRAVEL_INSURANCE_PAGE['WHO_GOING_DROPDOWN']
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_destination_dropdown(self, option_name):
        dropdown_locator = constants.TRAVEL_INSURANCE_PAGE['DESTINATION_DROPDOWN']
        dropdown_element = DropdownElement(dropdown_locator, self.driver)
        dropdown_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_start_date(self, date):
        date_picker_locator = constants.TRAVEL_INSURANCE_PAGE['START_DATE']
        date_picker_element = DatePickerElement(date_picker_locator, self.driver)
        date_picker_element.select_date_by_day(date)

    def click_and_select_end_date(self, date):
        date_picker_locator = constants.TRAVEL_INSURANCE_PAGE['END_DATE']
        date_picker_element = DatePickerElement(date_picker_locator, self.driver)
        date_picker_element.select_date_by_day(date)

    def click_show_result_button(self):
        show_result_button_locator = constants.TRAVEL_INSURANCE_PAGE['SHOW_RESULT_BUTTON']
        show_result_button_element = BaseElement(show_result_button_locator, self.driver)
        show_result_button_element.click()

    def wait_for_invisibility_of_loading_icon(self):
        self.driver.wait_for_invisibility_of_element_located(constants.SHARE_CONSTANTS['LOADING_ICON'])

