import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
valuex = browser.find_element_by_id("input_value")
x=valuex.text
y=calc(x)
stroka = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", stroka)
stroka.send_keys(y)
option1=browser.find_element_by_id("robotCheckbox")
option1.click()
option2=browser.find_element_by_id("robotsRule")
option2.click()
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()


