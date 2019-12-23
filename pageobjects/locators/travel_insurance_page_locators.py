from selenium.webdriver.common.by import By

DROPDOWN_LIST = {
    'POLICY_TYPE_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[1]'),
    'WHO_GOING_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[2]'),
    'DESTINATION_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[3]'),
    'DROPDOWN_OPTION': (By.XPATH, '(//span[text()="{option_name}"]/parent::a/parent::li)[1]'),
}

DATE_PICKERS = {
    'START_DATE': (By.NAME, 'startdate'),
    'END_DATE': (By.NAME, 'enddate'),
    'DATE_OPTION': (By.XPATH, '//td[contains(@class, "day")][text()="{day}"]'),
}

BUTTONS = {
    'SHOW_RESULT_BUTTON': (By.NAME, 'product-form-submit')
}
