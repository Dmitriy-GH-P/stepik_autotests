from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

url = "http://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    right_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    x_elem = browser.find_element(By.ID, "input_value")
    x = x_elem.text
    the_answer = str(math.log(abs(12*math.sin(int(x)))))

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(the_answer)

    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()


finally:
    alert = browser.switch_to.alert
    code = alert.text[alert.text.find(": ") + 2:]
    browser.quit()

print(code)