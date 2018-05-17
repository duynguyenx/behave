from selenium.webdriver.support.select import By

URL = {
    'LOGIN': '/login',
    'LOGOUT': '/logout'
}

LOG_IN = {
    'USERNAME_INPUTBOX': (By.NAME, 'username'),
    'PASSWORD_INPUTBOX': (By.NAME, 'password')
}
