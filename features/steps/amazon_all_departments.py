from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_url()


@when('hover over the "All Departments" dropdown menu')
def all_departments(context):
    context.app.header.all_departments()


@when('Select department {department}')
def select_department(context, department):
    context.app.header.select_department(department)


@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@then('verify search results are displayed')
def search_results_exist(context):
    context.app.header.search_results_exist()













@when('Wait for {sec} sec')
def wait_for_sec(context, sec):
    sleep(int(sec))


@when('Click Orders')
def click_orders(context):
    context.app.header.click_orders()








@then('Verify Sign in popup shown')
def verify_signin_popup_visible(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Signin btn not clickable'
    )


@then('Verify Sign in popup disappears')
def verify_signin_popup_not_visible(context):
    context.driver.wait.until_not(
        EC.visibility_of_element_located(SIGN_IN_BTN),
        message='Signin btn did not disappear'
    )


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    print('Before refresh:')
    print(context.ham_menu)
    context.driver.refresh()


@when('Click on ham menu')
def click_ham_menu(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    # print('After refresh:')
    # print(context.ham_menu)
    context.ham_menu.click()


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))  # '42'
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))  # => 42

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    print('\nLink count: ', len(footer_links))
    # assert 42 == 42
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'


@then('Verify Spanish option present')
def verify_lang_shown(context):
    context.app.header.verify_lang_shown()