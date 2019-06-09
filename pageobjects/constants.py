from selenium.webdriver.support.select import By

HOME_PAGE = {
    'INSURANCE_TAB': (By.CSS_SELECTOR, '[href="#Insurance"]'),
}

INSURANCE_PAGE = {
    'TRAVEL_TAB': (By.CSS_SELECTOR, '[href="#Travel"]'),
}

TRAVEL_INSURANCE_PAGE = {
    'POLICY_TYPE_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[1]'),
    'WHO_GOING_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[2]'),
    'DESTINATION_DROPDOWN': (By.XPATH, '(//span[@class="filter-option clearfix"])[3]'),
    'START_DATE': (By.NAME, 'startdate'),
    'END_DATE': (By.NAME, 'enddate'),
    'SHOW_RESULT_BUTTON': (By.NAME, 'product-form-submit')
}

TRAVEL_INSURANCE_RESULT_PAGE = {
    'ALL_CARD_BRAND_NAMES': (By.CSS_SELECTOR, '[data-gb-name="travel-plan"] .name'),
    'FILTER_VALUES': (By.CSS_SELECTOR, '.results-text small'),
}

SHARE_CONSTANTS = {
    'DROPDOWN_OPTION': (By.XPATH, '(//span[text()="{option_name}"]/parent::a/parent::li)[1]'),
    'DATE_OPTION': (By.XPATH, '//td[contains(@class, "day")][text()="{day}"]'),
    'LOADING_ICON': (By.CLASS_NAME, 'uil-rolling-css'),
}
