from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    @staticmethod
    def make_browser():
        chrome_options = Options()
        chrome_options.add_argument('disable-infobars')
        return webdriver.Chrome(chrome_options=chrome_options, executable_path='resources/chromedriver.exe')
