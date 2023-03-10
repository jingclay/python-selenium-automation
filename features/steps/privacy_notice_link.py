from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def original_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles

    context.driver.switch_to.window(windows[1])

    #context.original_window = context.driver.current_window_handle
    print('\nAFTER WE SWITCHED')
    print(context.original_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('switch back to original')
def switch_to_original(context):
    context.driver.switch_to.window(context.original_window)




