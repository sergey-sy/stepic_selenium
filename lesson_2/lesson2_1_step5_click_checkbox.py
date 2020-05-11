from selenium import webdriver
import time
import math


LINK = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    y_input = browser.find_element_by_css_selector('#answer')
    y_input.send_keys(y)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').submit()


finally:
    time.sleep(10)
    browser.quit()
