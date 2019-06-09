from datetime import datetime
from behave import *
from hamcrest import assert_that, equal_to
from helpers.data_helper import DataHelper
from pageobjects.travel_insurance_result_page import TravelInsuranceResultPage
from features.steps import constants


@then('the user should see 3 card brands "{result_list}" are displaying in the top 3 of Result Grid')
def step_verify_3_card_brands(context, result_list):
    actual_result = TravelInsuranceResultPage(context.browser).get_all_card_brand_names()[0:3]
    expected_result = DataHelper.get_list_from_string_list(result_list)
    assert_that(actual_result, equal_to(expected_result), 'Verify top 3 card brand names')


@then('the user should see the filter overview in Tralvel Insurance Search Result page is displaying users selected options correctly')
def step_verify_user_filter_options(context):
    actual_result = TravelInsuranceResultPage(context.browser).get_filter_overview_values()
    searched_options = context.travel_insurance_searched_options
    expected_result = searched_options['Policy Type'] + ' | ' + \
                      constants.TRAVEL_INSURANCE_CRITERIA_VALUES_MAPPING[searched_options['Whos Going']] + \
                      ' | travel to ' + searched_options['Destination'] + ' | from ' + \
    datetime.strptime(searched_options['Start Date'], '%d-%m-%Y').strftime('%d %b %Y') + ' to ' + \
    datetime.strptime(searched_options['End Date'], '%d-%m-%Y').strftime('%d %b %Y')

    assert_that(actual_result, equal_to(expected_result), 'Verify filter overview content')
