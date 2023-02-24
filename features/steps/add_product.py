
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@when('Click on stone maidens by Richards')
def click_stone_maidens(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/Stone-Maidens-Lloyd-Devereux-Richards/dp/161218605X/']").click()


@when('Click Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

@then('Click Cart icon from popup')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/cart/view.html?ref_=nav_cart']").click()

@then('Verify that stone maidens is present in the cart')
def verify_product_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/product/161218605X/']")



@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/product/161218605X/']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


