from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from pages.base_page import Page

class SigninPage(Page):

    def verify_signin_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin'

                                       )
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')

    def input_search_text(self,text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)


