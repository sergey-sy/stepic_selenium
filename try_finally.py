from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"


try:
    browser = webdriver.Chrome(executable_path="./chromedriver")
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()
finally:
    # close the browser even some mistakes in try block
    browser.quit()
