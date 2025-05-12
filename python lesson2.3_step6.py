from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    redirect_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    redirect_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_elem = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_elem.text
    my_answer = str(math.log(abs(12*math.sin(int(x)))))

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(my_answer)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    alert = browser.switch_to.alert
    my_code = alert.text[alert.text.find(": ") + 1:]
    browser.quit()
print(my_code)