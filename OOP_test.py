from selenium import webdriver
from OOP import LoginPage
import time

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(5)