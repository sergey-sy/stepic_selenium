from selenium import webdriver
import time


link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@name='first_name']")
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_xpath("//input[@name='last_name']")
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_xpath("//div[3]/input")
    input3.send_keys('Smolensk')
    input4 = browser.find_element_by_xpath("//input[@id='country']")
    input4.send_keys('Russia')
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
