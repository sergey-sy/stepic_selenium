import math
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LINK = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return math.log(abs(12 * math.sin( int(x) )))



browser = webdriver.Chrome(executable_path='../chromedriver')
browser.get(LINK)
browser.find_element_by_css_selector('[type="submit"]').submit()

try:
    alert = browser.switch_to.alert
    alert.accept()
except NoAlertPresentException:
    print('NoAlertPresentException')

x = WebDriverWait(browser, 2).until(
    EC.presence_of_element_located((By.ID, "input_value"))
)
calc_x = calc(x.text)
input_field = browser.find_element_by_id('answer')
input_field.send_keys(str(calc_x))
browser.find_element_by_css_selector('[type="submit"]').submit()

time.sleep(10)
browser.quit()
