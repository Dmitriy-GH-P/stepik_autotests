from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/selects1.html"
url2 = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    result_num = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result_num))

    time.sleep(1)

    button_submit = browser.find_element(By.CLASS_NAME, "btn-default")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
