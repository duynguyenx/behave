import os


class EnvSetup(object):

    # ENV VAR that defines the main URL (Domain)
    SITE = os.getenv('BASE_URL', 'http://site_address')

    # Environment variable of API host for data preparation
    API_HOST = os.getenv('API_URL', 'http://api_host:port')

    # Timeout for Selenium waits
    PUBLISHER_UPDATE_TIMEOUT_SECONDS = float(os.getenv('PUBLISHER_UPDATE_TIMEOUT_SECONDS', 45))
    PAGE_LOAD_TIMEOUT_SECONDS = float(os.getenv('PAGE_LOAD_TIMEOUT_SECONDS', 45))
    SELENIUM_TIMEOUT_SECONDS = float(os.getenv('SELENIUM_TIMEOUT_SECONDS', 15))
    PENDO_TIMEOUT_SECONDS = float(os.getenv('PENDO_TIMEOUT_SECONDS', 3))

    # Grid Environment details (Since our stagings are behind firewall, we always need to use sauce connect)
    # This define if you want to run the tests in a Grid/cloud service (like saucelabs, browserstack, etc)
    # Default is False to always run locally.
    GRID = os.getenv('GRID', False)
    PLATFORM = os.getenv('PLATFORM', 'LINUX')
    BROWSER_NAME = os.getenv('BROWSER_NAME', 'chrome')
    BROWSER_VERSION = os.getenv('BROWSER_VERSION', '50')
    TEST_NAME = os.getenv('TEST_NAME', '')
    BUILD_ID = os.getenv('BUILD_ID', '')
    TUNNEL_ID = os.getenv('TUNNEL_IDENTIFIER', '')
    GRID_HOST = os.getenv('SELENIUM_HOST', 'localhost')  # If sauce connect: localhost, else: ondemand.saucelabs.com
    GRID_PORT = os.getenv('SELENIUM_PORT', '4444')  # If sauce connect: 4445, else: 4444
    SAUCE_USER = os.getenv('SAUCE_USER_NAME', '')  # Saucelabs username
    SAUCE_KEY = os.getenv('SAUCE_API_KEY', '')  # Saucelabs api key

    # Reporting
    REPORT_FILE_PATH = os.getenv('REPORT_FILE_PATH', None)
    REPORT_SCENARIO_STATUS = os.getenv('REPORT_SCENARIO_STATUS', 'PASSED,FAILED,SKIPPED,UNTESTED')
