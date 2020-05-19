import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    book_house = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_house.click()
    input_value = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(calc(input_value)))
    browser.find_element_by_id('solve').click()
finally:
    time.sleep(10)
    browser.quit()
