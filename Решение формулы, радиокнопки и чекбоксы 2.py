import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
valuex_1 = browser.find_element_by_id("treasure")
valuex = valuex_1.get_attribute("valuex") 
y = calc(valuex)
input1=browser.find_element_by_id("answer")
input1.send_keys(y)
option1=browser.find_element_by_id("robotCheckbox")
option1.click()
option2=browser.find_element_by_id("robotsRule")
option2.click()
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()