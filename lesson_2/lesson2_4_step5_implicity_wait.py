import time
from selenium import webdriver


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')

    browser.implicitly_wait(5)

    browser.get('http://suninjuly.github.io/wait1.html')
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    time.sleep(5)
    browser.quit()
