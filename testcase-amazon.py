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

driver.quit()
print('test case passed')
