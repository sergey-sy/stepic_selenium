import time
import math

from selenium import webdriver


LINK = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK)
    browser.find_element_by_css_selector('[type="submit"]').click()
    browser.switch_to.window(browser.window_handles[-1])
    x_text = browser.find_element_by_id('input_value').text

    browser.find_element_by_id('answer').send_keys(str(calc(x_text)))
    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()
