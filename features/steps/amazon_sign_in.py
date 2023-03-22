from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):

    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")

    def verify_search_result(self,expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULTS)



