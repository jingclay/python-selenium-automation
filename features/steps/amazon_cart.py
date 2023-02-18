from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Cart icon from popup')
def cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify Your Amazon Cart is Empty')
def verify_cart_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'







