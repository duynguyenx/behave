from conf.env_setup import EnvSetup
from pageobjects.locators import travel_insurance_page_locators as locators
from pageobjects.core.elements import Element


class DropdownElement(Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_option_by_option_name(self, option_name, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, move_to_element=False):
        option_locator = locators.DROPDOWN_LIST['DROPDOWN_OPTION']
        option_locator = (option_locator[0], option_locator[1].format(option_name=option_name))
        self.select_option_option_locator(option_locator, timeout, move_to_element)

    def select_option_option_locator(self, option_locator, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS,
                                     move_to_element=False):
        self.click(timeout)
        option_element = Element(option_locator, self._driver)
        option_element.click(timeout, move_to_element)
