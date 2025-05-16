import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nopen browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nclosing browser after the test")
    browser.quit()


def stepik_login(browser):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "ember466"))).click()
    browser.find_element(By.NAME, "login").send_keys("Your login...")
    browser.find_element(By.NAME, "password").send_keys("Your password...")
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize("link", links)
def test_alot_of_tasks(browser, link):
    browser.get(link)
    stepik_login(browser)

    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area")))
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(str(answer))

    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    result = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

    assert result == "Correct!", f'Result is ({result})'
    # Из 8 тестов 3 должны упасть
    # А в результате будет содержаться кусочек фразы
    # Ответом задачи будет вся фраза