from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_redirect.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # button = browser.find_element_by_tag_name("button")
    # button.click()
    #
    # confirm = browser.switch_to.alert()
    # confirm.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
