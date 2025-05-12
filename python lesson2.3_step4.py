from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    click_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    click_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_elem = browser.find_element(By.ID, "input_value")
    x = x_elem.text

    my_answer = str(math.log(abs(12*math.sin(int(x)))))

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(my_answer)

    button_submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
