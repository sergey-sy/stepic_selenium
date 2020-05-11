from selenium import webdriver
from selenium.webdriver.common import by
import time


link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(link)

    mandatory_inputs = [
        browser.find_element_by_css_selector(selector) for selector in [
                                                                        ".first_block .first",
                                                                        ".first_block .second",
                                                                        ".first_block .third",
                                                                        ]
    ]

    [elem.send_keys('test_text') for elem in mandatory_inputs]

    button = browser.find_element(by.By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(2)

    welcome_text = browser.find_element_by_tag_name('h1').text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
