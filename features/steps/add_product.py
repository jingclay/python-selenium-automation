from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):

    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")

    def verify_search_result(self,expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULTS)


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_url()


@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click on stone maidens by Richards')
def click_stone_maidens(context):
    context.app.search_results_page.click_stone_maidens()


@when('Click Add to Cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@then('Click Cart icon from popup')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then ('Verify that stone maidens is present in the cart')
def stone_maidens_present(context):
    context.app.search_results_page.stone_maidens_present()




