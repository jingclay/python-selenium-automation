from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Returns & Orders from popup')
def click_returns(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()


@then('Verify Sign In header is visible')
def verify_sign_in_header(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify email input field is present')
def verify_email_input(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']")




