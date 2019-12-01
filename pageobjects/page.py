from conf.env_setup import EnvSetup
from pageobjects import constants
from pageobjects.driver import Driver


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        if not isinstance(driver, Driver):
            self._driver = Driver(driver)
        else:
            self._driver = driver

    def quit(self):
        self._driver.quit()

    def maximize_window(self):
        self._driver.maximize_window()

    def find_element(self, tuple_selector):
        return self._driver.find_element(*tuple_selector)

    def find_elements(self, tuple_selector):
        element_list = self._driver.find_elements(*tuple_selector)
        return element_list

    @property
    def driver(self):
        return self._driver


class BaseElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, locator, driver):
        if not isinstance(driver, Driver):
            self._driver = Driver(driver)
        else:
            self._driver = driver
        self._locator = locator
        self._web_element = None

    def click(self, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, move_to_element=False, move_to_element_by_script=False,
              by_script=False):
        if move_to_element or move_to_element_by_script:
            self._driver.move_to_element(self._locator, move_to_element_by_script)

        self._web_element = self._driver.wait_for_element_to_be_clickable(self._locator, timeout)
        if by_script:
            self._driver.execute_script('arguments[0].click();', self._web_element)
        else:
            self._web_element.click()

    def send_keys(self, *keys):
        self._web_element = self._driver.wait_for_visibility_of_element_located(self._locator)
        for key in keys or []:
            self._web_element.send_keys(key)

    def get_text(self):
        self._web_element = self._driver.wait_for_element_to_be_presented(self._locator)
        return self._web_element.text

    def get_attribute(self, attribute, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, move_to_element=False):
        if move_to_element:
            self._driver.move_to_element(self._locator)
        self._web_element = self._driver.wait_for_element_to_be_presented(self._locator, timeout)
        return self._web_element.get_attribute(attribute)

    @property
    def web_element(self):
        return self._driver.wait_for_element_to_be_presented(self._locator)

    def find_element(self, tuple_selector):
        return self.web_element.find_element(tuple_selector)

    def find_elements(self, tuple_selector):
        return self.web_element.find_elements(tuple_selector)


class DropdownElement(BaseElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # just ez for use
    def select_option_by_option_name(self, option_name, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, move_to_element=False):
        option_locator = constants.SHARE_CONSTANTS['DROPDOWN_OPTION']
        option_locator = (option_locator[0], option_locator[1].format(option_name=option_name))
        self.select_option_option_locator(option_locator, timeout, move_to_element)

    def select_option_option_locator(self, option_locator, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS,
                                     move_to_element=False):
        self.click(timeout)
        option_element = BaseElement(option_locator, self._driver)
        option_element.click(timeout, move_to_element)


class DatePickerElement(BaseElement):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_date_by_day(self, day):
        day_locator = constants.SHARE_CONSTANTS['DATE_OPTION']
        day_locator = (day_locator[0], day_locator[1].format(day=day))
        self.select_date_by_day_locator(day_locator)

    def select_date_by_day_locator(self, day_locator):
        self.click()
        day_element = BaseElement(day_locator, self._driver)
        day_element.click(move_to_element=True)
