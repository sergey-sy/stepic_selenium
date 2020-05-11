from selenium import webdriver
import time


link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(link)
    [elem.send_keys('a') for elem in browser.find_elements_by_tag_name('input')]

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
