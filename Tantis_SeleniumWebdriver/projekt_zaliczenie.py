import unittest
from telnetlib import EC
from selenium import webdriver
from faker import Faker
from time import sleep
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker("pl_PL")
valid_name = fake.first_name()
valid_last_name = fake.last_name()
valid_email = fake.email()
valid_password = fake.password(length=9)
cart2items = 2

class TantisRegistration(unittest.TestCase):
     def setUp(self):
       # Warunki wstępne:
       # Uruchomiona przeglądarka
       # Przeglądarka otwarta na stronie: https://tantis.pl/
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.get("http://tantis.pl/")

     def tearDown(self):
       self.driver.quit()

     def test_registration(self):
       #Rejestracja nowego użytkownika bez akceptacji regulaminu
       #KROKI:
       driver = self.driver
       #.1.Wybor opcji logowania/rejestracji
       logowanie_button = driver.find_element(By.ID, "navbarDropdown")
       logowanie_button.click()
       #2.Rejestracja - utworzenie nowego konta
       rejestracja_button = driver.find_element(By.LINK_TEXT, "zarejestruj")
       rejestracja_button.click()
       sleep(5)
       #3. Uzupelnienie imienia
       name_field = driver.find_element(By.ID, "registrationFirstName").send_keys(valid_name)
       #4. Uzupelnienie nazwiska
       last_name_field = driver.find_element(By.ID, "registrationLastName").send_keys(valid_last_name)
       #5. Uzupelnienie adresu e-mail
       email_field = driver.find_element(By.ID, "registrationEmail").send_keys(valid_email)
       #6. Uzupelnienie hasla
       password_field = driver.find_element(By.ID, "registrationPassword").send_keys(valid_password)
       #7. Potwierdzenie zalozenia konta
       zaloz_konto = driver.find_element(By.ID, "registerUserBtn")
       zaloz_konto.click()
       #8. Screenshot z widocznym bledem - brakiem akceptacji regulaminy
       driver.save_screenshot("screenshot.png")
       sleep(5)
       # ASSERTION:
       # 1. Szukanie wszystkich komunikatów o błędzie
       error_messages = self.driver.find_elements(By.ID, "acceptTerms-error")
       # 2. Sprawdzenie, czy jest tylko jeden taki komunikat
       self.assertEqual(1, len(error_messages))
       # 3. Sprawdenie tresci i widoczność komunikatu "To pole jest wymagane"
       # print(error_messages[0].text)
       self.assertEqual("To pole jest wymagane.",
                        error_messages[0].text)
       # 4. Srawdzam, czy ten komunikat jest pod polem "hasło"
       error_msg_locator = locate_with(By.ID, "acceptTerms-error")
       error_msg = self.driver.find_element(error_msg_locator)
       # Spradzam, czy error_msg to ten sam element, co error_messages[0]
       assert error_messages[0].id == error_msg.id
       sleep(5)

class AddToCart(unittest.TestCase):
     def setUp(self):
       # Warunki wstępne:
       # Uruchomiona przeglądarka
       # Przeglądarka otwarta na stronie: https://tantis.pl/
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.get("http://tantis.pl/")

     def tearDown(self):
       self.driver.quit()

     def test_add_to_cart(self):
       # KROKI:
       driver = self.driver
       # 1. Znalezienie na stronie pola wyszukiwania i wpisanie ("Harry Potter i Komnata Tajemnic")
       search_field = driver.find_element(By.ID, "search").send_keys("Harry Potter i Komnata Tajemnic")
       search_magnifier = driver.find_element(By.ID, "searchBtn")
       search_magnifier.click()
       sleep(10)
       search_item1 = driver.find_element(By.XPATH, ('//*[@id="productGridRow"]/div[1]/div/div[1]/div/div/div[1]/div/a/img'))
       search_item1.click()
       # 2. Dodanie 1. przedmiotu do koszyka
       add_to_cart = driver.find_element(By.ID, "addToCartSidebar")
       add_to_cart.click()
       sleep(10)
       close_cart_notification = driver.find_element(By.CLASS_NAME, "continue-shopping-link")
       close_cart_notification.click()
       sleep(5)
       # 3. Znalezienie na stronie pola wyszukiwania i wpisanie ("Harry Potter i Czara Ognia")
       search_field = driver.find_element(By.ID, "search").send_keys("Harry Potter i Czara Ognia")
       sleep(10)
       search_magnifier = driver.find_element(By.ID, "searchBtn")
       search_magnifier.click()
       sleep(10)
       search_item2 = driver.find_element(By.XPATH, ('//*[@id="productGridRow"]/div[1]/div/div[1]/div/div/div[1]/div/a/img'))
       search_item2.click()
       # 4. Dodanie 2. przedmiotu do koszyka
       add_to_cart = driver.find_element(By.ID, "addToCartSidebar")
       add_to_cart.click()
       sleep(10)
       # 4. Sprawdzenie czy liczba przedmiotow w koszyku sie zgadza
       show_cart = driver.find_element(By.XPATH, ('//*[@id="addedToCartSuccessContent"]/div[3]/div/div[2]/a'))
       show_cart.click()
       sleep(5)
       driver.save_screenshot("cart_view.png")
       #ASSERTION
       items_in_cart = driver.find_elements(By.CLASS_NAME, "cart-item-container")
       quantity_of_items = 0
       for x in items_in_cart:
         quantity_of_items = (quantity_of_items + 1)
       self.assertEqual(cart2items, quantity_of_items)
       print("Ilość produktów w koszyku: ", quantity_of_items)
