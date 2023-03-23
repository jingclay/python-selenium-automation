from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RESULTS_HEADER = (By.XPATH, "//span[.='RESULTS']")
    ALL_DEPT = (By.ID, 'searchDropdownBox')
    FOOD_READY = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.XPATH, "//div[@class='nav-search-submit nav-sprite']//input[@type='submit']")
    SUBNAV= (By.CSS_SELECTOR,"#nav-subnav[data-category={CATEGORY}]")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def get_subnav_locator(self,category):
        return[self.SUBNAV[0],self.SUBNAV[1].replace('{CATEGORY},category')]

    def all_departments(self):
        all_department_options = self.find_element(*self.ALL_DEPT)
        actions = ActionChains(self.driver)
        actions.move_to_element(all_department_options)
        actions.perform()


    def verify_selected_dept(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)

    def search_results_exist(self):
        self.find_element(*self.RESULTS_HEADER)

    def select_department(self, department):
        select_department = (By.XPATH, f"//select[@id='searchDropdownBox']//option[.='{department}']")

        self.find_element(*select_department)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    # def click_search(self):
    #     self.find_element(*self.SEARCH_BAR)

