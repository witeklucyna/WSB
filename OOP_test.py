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
#make_screenshot()
try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
except AssertionError:
    print('Assercja nie przeszla')
else:
    print('Asercja przeszla')
finally:
    print('po asercji')
    driver.quit()