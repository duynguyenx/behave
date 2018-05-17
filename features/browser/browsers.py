from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from conf.env_setup import EnvSetup


class Browser:

    @staticmethod
    def make_browser():

        desired_capability = {
            'platform': EnvSetup.PLATFORM,
            'browserName': EnvSetup.BROWSER_NAME,
            # 'version': EnvSetup.BROWSER_VERSION
            # Saucelabs specific configuration below:
            # 'name': EnvSetup.TEST_NAME,
            # 'build': EnvSetup.BUILD_ID,
            # 'recordVideo': True,
            # 'recordScreenshots': True,
            # 'recordLogs': True,
            # 'tunnelIdentifier': EnvSetup.TUNNEL_ID,
            # "maxDuration": 3600
            }

        if EnvSetup.GRID:
            grid_source = 'http://{host}:{port}/wd/hub'.format(host=EnvSetup.GRID_HOST, port=EnvSetup.GRID_PORT)
            browser = webdriver.Remote(command_executor=grid_source, desired_capabilities=desired_capability)
        else:
            chrome_options = Options()
            chrome_options.add_argument('disable-infobars')
            chrome_options.add_argument("--start-maximized")
            browser = webdriver.Chrome(chrome_options=chrome_options)
        return browser
