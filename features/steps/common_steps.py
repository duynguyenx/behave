from behave import given, when
from conf.env_setup import EnvSetup
from pageobjects.home_page import HomePage
from pageobjects.insurance_page import InsurancePage


@given('the user is standing at home page')
def step_visit_home_page(context):
    context.browser.get(EnvSetup.BASE_URL)


@when('the user clicks on Insurance tab')
def click_on_insurance_tab(context):
    HomePage(context.browser).click_insurance_tab()


@when('the user clicks on Travel tab')
def click_on_travel_tab(context):
    InsurancePage(context.browser).click_travel_tab()
