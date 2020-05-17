from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


LINK_1 = 'http://suninjuly.github.io/selects1.html'
LINK_2 = 'http://suninjuly.github.io/selects2.html'


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK_1)
    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    sum_value = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_value))
    browser.find_element_by_css_selector('button[type="submit"]').submit()
finally:
    time.sleep(10)
    browser.quit()
