from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    x_elem = browser.find_element(By.ID, "input_value")
    x = x_elem.text

    answer_number = str(math.log(abs(12*math.sin(int(x)))))

    browser.execute_script("window.scrollBy(0, 100);")

    my_answer = browser.find_element(By.ID, "answer")
    my_answer.send_keys(answer_number)

    check_box = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check_box.click()

    radio_button = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_button.click()

    button_submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
