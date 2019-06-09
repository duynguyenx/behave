import os


class EnvSetup(object):

    # ENV VAR that defines the main URL
    BASE_URL = os.getenv('BASE_URL', 'https://www.gobear.com/ph?x_session_type=UAT')

    # Timeout for Selenium waits
    WAIT_TIMEOUT_SECONDS = float(os.getenv('WAIT_TIMEOUT_SECONDS', 15))
