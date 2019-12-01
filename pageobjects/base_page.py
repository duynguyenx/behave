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
