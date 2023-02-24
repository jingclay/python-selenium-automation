from selenium.webdriver.common.by import By

from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('click best sellers')
def click_best_seller(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/']").click()


@then('Verify that best seller has {expected_amount} links')
def verify_best_seller_links_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))  # '42'
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))  # => 42

    best_seller_links = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header a")

    print(best_seller_links)
    print('\nLink count: ', len(best_seller_links))
    # assert 5 == 5
    assert len(best_seller_links) == expected_amount, f'Expected {expected_amount} links, but got {len(best_seller_links)}'


