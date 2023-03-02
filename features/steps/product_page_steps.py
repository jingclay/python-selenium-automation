from selenium.webdriver.common.by import By

from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through {colors} colors')
def verify_user_can_select_colors(context, colors):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = colors.split(', ')

    actual_colors = []
    for color in all_color_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

