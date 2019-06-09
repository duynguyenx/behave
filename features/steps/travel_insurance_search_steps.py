from datetime import datetime
from behave import *
from helpers.data_helper import DataHelper
from pageobjects.travel_insurance_page import TravelInsurancePage


@when('the user clicks on Show my Results button')
def step_show_result_button(context):
    TravelInsurancePage(context.browser).click_show_result_button()
    TravelInsurancePage(context.browser).wait_for_invisibility_of_loading_icon()


@when('the user selected below options in Travel Insurance Search box')
def step_show_result_button(context):
    input_criteria = DataHelper.exclude_dictionary(DataHelper.convert_key_value_table_to_dictionary(context.table))
    context.travel_insurance_searched_options = {}
    if 'Policy Type' in input_criteria:
        TravelInsurancePage(context.browser).click_and_select_policy_dropdown(input_criteria['Policy Type'])
        context.travel_insurance_searched_options.update({'Policy Type': input_criteria['Policy Type']})
    if 'Whos Going' in input_criteria:
        TravelInsurancePage(context.browser).click_and_select_whos_going_dropdown(input_criteria['Whos Going'])
        context.travel_insurance_searched_options.update({'Whos Going': input_criteria['Whos Going']})
    if 'Destination' in input_criteria:
        TravelInsurancePage(context.browser).click_and_select_destination_dropdown(input_criteria['Destination'])
        context.travel_insurance_searched_options.update({'Destination': input_criteria['Destination']})
    if 'Start Date' in input_criteria:
        start_date = datetime.strptime(input_criteria['Start Date'], '%d-%m-%Y')
        day = start_date.date().day
        TravelInsurancePage(context.browser).click_and_select_start_date(day)
        context.travel_insurance_searched_options.update({'Start Date': input_criteria['Start Date']})
    if 'End Date' in input_criteria:
        end_date = datetime.strptime(input_criteria['End Date'], '%d-%m-%Y')
        day = end_date.date().day
        TravelInsurancePage(context.browser).click_and_select_end_date(day)
        context.travel_insurance_searched_options.update({'End Date': input_criteria['End Date']})
