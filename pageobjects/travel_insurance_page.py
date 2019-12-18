from pageobjects.core import BasePage
from pageobjects.core.elements import DropdownElement, DatePickerElement, Element
from pageobjects.core.enums import WaitType
from pageobjects.locators import travel_insurance_page_locators as locators, common_locators


class TravelInsurancePage(BasePage):
    def click_and_select_policy_dropdown(self, policy_name):
        policy_element = DropdownElement(locators.DROPDOWN_LIST['POLICY_TYPE_DROPDOWN'], self.driver)
        policy_element.select_option_by_option_name(policy_name, move_to_element=True)

    def click_and_select_whos_going_dropdown(self, option_name):
        who_going_element = DropdownElement(locators.DROPDOWN_LIST['WHO_GOING_DROPDOWN'], self.driver)
        who_going_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_destination_dropdown(self, option_name):
        destination_element = DropdownElement(locators.DROPDOWN_LIST['DESTINATION_DROPDOWN'], self.driver)
        destination_element.select_option_by_option_name(option_name, move_to_element=True)

    def click_and_select_start_date(self, date):
        DatePickerElement(locators.DATE_PICKERS['START_DATE'], self.driver).select_date_by_day(date)

    def click_and_select_end_date(self, date):
        DatePickerElement(locators.DATE_PICKERS['END_DATE'], self.driver).select_date_by_day(date)

    def click_show_result_button(self):
        Element(locators.BUTTONS['SHOW_RESULT_BUTTON'], self.driver).click()

    def wait_for_invisibility_of_loading_icon(self):
        self.wait_elements(common_locators.LOADING_ICON, WaitType.WAIT_FOR_INVISIBILITY_OF_ELEMENT_LOCATED)
