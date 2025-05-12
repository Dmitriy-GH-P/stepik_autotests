from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/huge_form.html'
try:
    browser = webdriver.Chrome()
    browser.get(url)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for elem in elements:
        elem.send_keys('Да')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

