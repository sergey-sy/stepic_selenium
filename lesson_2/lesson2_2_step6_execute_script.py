from selenium import webdriver
import math
import time


LINK_1 = 'http://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x_value)))))


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK_1)
    x_value = browser.find_element_by_id('input_value').text
    answer = str(calc(x_value))
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').submit()
finally:
    time.sleep(10)
    browser.quit()
