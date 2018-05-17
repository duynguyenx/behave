import logging
from features.hooks.data_storage import DataStorage
from features.hooks.report.report_helper import ReportHelper
from conf.env_setup import EnvSetup
from features.hooks.gmail.gmail_helper import GmailHelper
record = dict()


def before_all(context):
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARN)
    # context.gmail_helper = GmailHelper()


def before_feature(context, feature):
    """
    Placeholder for any before feature hooks needed
    """


def before_scenario(context, scenario):
    case_id = str(scenario.tags[0])
    if not record.get('current_case_id', None):
        record['current_case_id'] = case_id
    context = init_browser_session(context)
    context.browser.maximize_window()


def init_browser_session(context):
    from features.browser.browsers import Browser
    context.browser = Browser().make_browser()
    # context.data_storage = DataStorage(context)
    # context.data_storage.store_session(context)
    return context


def after_scenario(context, scenario):
    if EnvSetup.REPORT_FILE_PATH:
        ReportHelper.write_scenario_summary(context, scenario, EnvSetup.REPORT_FILE_PATH)
    # context.data_storage.store_session(context)
    # context.data_storage.cleanup(context)
    context.browser.quit()


def after_all(context):
    """
    Placeholder for any before feature hooks needed
    """
    pass
