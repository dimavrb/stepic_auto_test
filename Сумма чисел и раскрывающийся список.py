from selenium import webdriver
import math
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
value_1 = browser.find_element_by_id("num1")
x = value_1.text
value_2 = browser.find_element_by_id("num2")
y = value_2.text
summ=str(int(x)+int(y))
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(summ)
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()