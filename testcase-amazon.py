from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

service = Service('/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

# orders
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()
driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]")
driver.find_element(By.XPATH, "//input[@id='ap_email']")

expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH,  "//h1[contains(text(),'Sign in')]").text
print(actual_result)
assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


print('test case passed')
driver.quit()
