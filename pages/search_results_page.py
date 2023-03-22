
from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    CLICK_SEARCH = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart-count')
    SHOPPING_CART_EMPTY = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")
    CLICK_STONE_MAIDENS = (By.CSS_SELECTOR, "a[href*='/Stone-Maidens-Lloyd-Devereux-Richards/dp/161218605X/']")
    CLICK_ADD_TO_CART = (By.XPATH, "//input[@id='add-to-cart-button']")
    CLICK_CART_ICON = (By.CSS_SELECTOR, "a[href*='/gp/cart/view.html?ref_=nav_cart']")
    STONE_MAIDENS_PRESENT = (By.CSS_SELECTOR, "a[href*='/gp/product/161218605X/']")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_add_to_cart(self):
        self.click(*self.CLICK_ADD_TO_CART)

    def click_stone_maidens(self):
        self.click(*self.CLICK_STONE_MAIDENS)

    def click_cart_icon(self):
        self.click(*self. CLICK_CART_ICON)

    def stone_maidens_present(self):
        self.find_element(*self.STONE_MAIDENS_PRESENT)






