from selenium import webdriver
import time
import os


LINK = 'http://suninjuly.github.io/file_input.html'


try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(LINK)
    browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Name')
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Surname')
    browser.find_element_by_css_selector('input[name="email"]').send_keys('email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_for_send.txt')

    file_input = browser.find_element_by_css_selector('input[type="file"]')
    file_input.send_keys(file_path)
    browser.find_element_by_css_selector('button[type="submit"]').submit()
finally:
    time.sleep(10)
    browser.quit()


