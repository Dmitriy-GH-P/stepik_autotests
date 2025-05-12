from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x_elem = browser.find_element(By.ID, 'treasure')
    x_elem_value = x_elem.get_attribute("valuex")
    x = x_elem_value
    right_answer = str(math.log(abs(math.sin(int(x)) * 12)))

    time.sleep(1)

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(right_answer)

    time.sleep(1)

    check_box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_box.click()

    time.sleep(1)

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    time.sleep(1)

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
