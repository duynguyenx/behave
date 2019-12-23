from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conf.env_setup import EnvSetup
from pageobjects.core.enums import WaitType


class Driver:

    def __init__(self, selenium_webdriver):
        self._driver = selenium_webdriver

    def quit(self):
        self._driver.quit()

    def maximize_window(self):
        self._driver.maximize_window()

    def find_element(self, tuple_selector):
        return self._driver.find_element(*tuple_selector)

    def find_elements(self, tuple_selector):
        return self._driver.find_elements(*tuple_selector)

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_invisibility_of_element_located(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_element_to_be_presented(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self._driver, timeout)
        elements = wait.until(EC.presence_of_element_located(tuple_selector))
        return elements

    def wait_for_elements_to_be_presented(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self._driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(tuple_selector))
        return elements

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    def execute_script(self, script, *args):
        self._driver.execute_script(script, *args)

    def move_to_element(self, tuple_selector, by_script=False):
        element = self.wait_for_element_to_be_presented(tuple_selector)
        if by_script:
            self.execute_script("arguments[0].scrollIntoView(true);", element)
        else:
            actions = ActionChains(self._driver)
            actions.move_to_element(element)
            actions.perform()


WAIT_MAPPING = {
    WaitType.WAIT_FOR_VISIBILITY_OF_ELEMENT_LOCATED: Driver.wait_for_visibility_of_element_located,
    WaitType.WAIT_FOR_INVISIBILITY_OF_ELEMENT_LOCATED: Driver.wait_for_invisibility_of_element_located,
    WaitType.WAIT_FOR_ELEMENT_TO_BE_PRESENTED: Driver.wait_for_element_to_be_presented,
    WaitType.WAIT_FOR_ELEMENTS_TO_BE_PRESENTED: Driver.wait_for_elements_to_be_presented,
    WaitType.WAIT_FOR_ELEMENTS_TO_BE_CLICKABLE: Driver.wait_for_element_to_be_clickable,
}
