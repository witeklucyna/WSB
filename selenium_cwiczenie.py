from selenium import webdriver
import time
import datetime

def make_screenshot(okno_przegladarki):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('%H%M%S')+' .png'
    okno_przegladarki.get_screenshot_as_file(screenshot)

if __name__=='__main__':
    driver = webdriver.Chrome()   #driver to okno przegladarki
    driver.get('https://google.com')
    print('Nazwa strony',driver.title)
    time.sleep(5)
    button1_accept = driver.find_element('id', 'L2AGLb')
    button1_accept.click()
    print(button1_accept)
    time.sleep(5)
    search_field = driver.find_element('name','q')
    search_field.send_keys('Czy jutro jest niedziela handlowa?')
    #search.field.send_keys(Keys.ENTER)
    search_button = driver.find_element('name', 'btnK')
    search_button.submit()
    driver.quit()

# driver2 = webdriver.Edge()
# time.sleep(3)