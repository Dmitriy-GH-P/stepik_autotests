from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

url = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(url)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Ivan")

    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Demidov")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Demidov.SPB@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    uploading_my_file = browser.find_element(By.ID, "file")
    uploading_my_file.send_keys(file_path)

    button_submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
