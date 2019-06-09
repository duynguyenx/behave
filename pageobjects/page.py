from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conf.env_setup import EnvSetup
from pageobjects import constants


class Page:

    def __init__(self, selenium_webdriver):
        self.driver = selenium_webdriver

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def find_elements(self, tuple_selector):
        element_list = self.driver.find_elements(*tuple_selector)
        return element_list

    # ========================== wait elements ===============================================
    def wait_for_visibility_of_element(self, by, selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, selector)))

    def wait_for_text_to_be_present(self, by, selector, text, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element((by, selector), text))

    def wait_for_element_to_click(self, by, selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, selector)))

    def get_text(self, by, selector):
        element = self.wait_for_visibility_of_element(by, selector)
        return element.text

    def move_to_element(self, tuple_selector, by_script=False):
        element = self.wait_element_exist(tuple_selector)
        if by_script:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.perform()

    # ---- wait methods ------------

    def wait_element_exist(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(tuple_selector))

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_invisibility_of_element_located(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_text_to_be_present_in_element(self, tuple_selector, text, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(tuple_selector, text))

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    # ---- action methods ------------

    def click_element(self, tuple_selector, move_to_element=False, move_to_element_by_script=False,
                      timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, by_script=False):
        if move_to_element:
            self.move_to_element(tuple_selector)
        if move_to_element_by_script:
            self.move_to_element(tuple_selector, by_script=True)
        element = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
        if by_script:
            self.driver.execute_script("arguments[0].click();", element)
            self.driver.execute_script("return arguments[0].style", element)
        else:
            element.click()

    def type_text(self, tuple_selector, value=None, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        if value:
            element.send_keys(value)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    # ---- get information methods ------------
    def get_element_text(self, tuple_selector, move_to_element=False, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)

        return element.text

    def get_text_of_elements(self, tuple_selector, move_to_element=False, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(tuple_selector))
        if not move_to_element:
            return self.get_text_list(elements)
        text_list = []
        for e in elements:
            ActionChains(self.driver).move_to_element(e).perform()
            text_list.append(str(e.text))
        return text_list

    def get_attribute_of_element(self, tuple_selector, attribute, timeout=EnvSetup.WAIT_TIMEOUT_SECONDS,
                                 move_to_element=False):
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_element_exist(tuple_selector, timeout)
        return element.get_attribute(attribute)

    @staticmethod
    def get_text_list(list_data):
        name_list = []
        for item in list_data:
            name_list.append(item.text)
        return name_list

    # ---- Application common methods ------------

    def click_and_select_option_from_dropdown(self, dropdown_locator, option_name,
                                              timeout=EnvSetup.WAIT_TIMEOUT_SECONDS, move_to_element=False):
        self.click_element(dropdown_locator, timeout)
        option_locator = constants.SHARE_CONSTANTS['DROPDOWN_OPTION']
        option_locator = (option_locator[0], option_locator[1].format(option_name=option_name))
        self.click_element(option_locator, move_to_element=move_to_element)

    def select_date_on_date_picker(self, day):
        day_locator = constants.SHARE_CONSTANTS['DATE_OPTION']
        day_locator = (day_locator[0], day_locator[1].format(day=day))
        self.click_element(day_locator, move_to_element=True)

    def wait_for_invisibility_of_loading_icon(self):
        self.wait_for_invisibility_of_element_located(constants.SHARE_CONSTANTS['LOADING_ICON'])
