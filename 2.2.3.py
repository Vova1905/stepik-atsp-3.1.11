from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_el = browser.find_element_by_id("num1")
    num2_el = browser.find_element_by_id("num2")
    num1 = int(num1_el.text)
    num2 = int(num2_el.text)

    sum = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
