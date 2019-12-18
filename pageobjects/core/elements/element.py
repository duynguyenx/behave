from conf.env_setup import EnvSetup
from pageobjects.core.driver import Driver


class Element(object):
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
