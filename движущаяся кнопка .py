import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
valuex= browser.find_element_by_id("input_value")
x = valuex.text
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()
