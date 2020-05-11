import time
import math
from selenium import webdriver


LINK = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK)
    treasure_img = browser.find_element_by_css_selector('#treasure')
    value_x = treasure_img.get_attribute('valuex')
    x = calc(int(value_x))
    browser.find_element_by_css_selector('#answer').send_keys(x)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').submit()

finally:
    time.sleep(10)
    browser.quit()
