from behave import *
from features.pageobjects.login import constants as lc
from conf.env_setup import EnvSetup
from features.pageobjects.login.login import LoginPage


@given('the user is in the login page')
def step_visit_login_page(context):
    context.browser.get(EnvSetup.SITE + lc.URL['LOGIN'])


@step('the user input username "{username}"')
def step_input_user_name(context, username):
    LoginPage(context.browser).input_username(username)


@step('the user input password "{password}"')
def step_input_password(context, password):
    LoginPage(context.browser).input_password(password)
