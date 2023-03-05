from selenium import webdriver
from selenium_cwiczenie import make_screenshot
from OOP import LoginPage
import time

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
time.sleep(2.5)
page.enter_username('standard_user')
time.sleep(2.5)
page.enter_password('secret_sauce')
time.sleep(2.5)
page.click_login()
time.sleep(2.5)
make_screenshot()
driver.quit()