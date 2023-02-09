from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//a[@data-nav-role='signin']").click()

# logo
logo = driver.find_element(By.CLASS_NAME, 'a-icon-logo')

assert logo.accessible_name == 'Amazon'
assert logo.aria_role == 'img'

# continue_button
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
assert continue_button.tag_name == 'input'

# help_link
help_link = driver.find_element(By.XPATH, "//span[contains(text(),'Need help')]/..")

assert help_link.tag_name == 'a'

# Forgot your password link
forgot_your_password_link = driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password')]/..")

# Other_issues_with_Sign_In_link
other_issues_with_Sign_In_link = driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
create_your_Amazon_account_button = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Conditions_of_use_link
conditions_of_use_link = driver.find_element(By.XPATH, "//a[contains(text(),'Conditions of Use')]")

#Privacy Notice link
privacy_notive_link = driver.find_element(By.XPATH,"//a[contains(text(),'Privacy Notice')]")




