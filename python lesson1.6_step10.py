from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    first_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_input.send_keys('Ivan')

    second_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    second_input.send_keys('Demidov')

    third_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    third_input.send_keys('Demidov@mail.ru')

    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()