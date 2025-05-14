from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

result = "Congratulations! You have successfully registered!"

class TestSubscribe(unittest.TestCase):
     def check_page(self, link):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)

        first_input = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_input.send_keys('Ivan')

        second_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        second_input.send_keys('Demidov')

        third_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        third_input.send_keys('Demidov@mail.ru')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        browser.quit()

        return welcome_text

    def test_first_link(self):
        self.assertEqual(self.check_page("http://suninjuly.github.io/registration1.html"), result)

    def test_second_link(self):
        self.assertEqual(self.check_page("http://suninjuly.github.io/registration2.html"), result)

if __name__ == "__main__":
    unittest.main()
