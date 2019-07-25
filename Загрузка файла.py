import math
import os 
from selenium import webdriver
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
inputname=browser.find_element_by_name("firstname")
inputname.send_keys("Дмитрий")
inputsname=browser.find_element_by_name("lastname")
inputsname.send_keys("Калинин")
inputmail=browser.find_element_by_name("email")
inputmail.send_keys("dima@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'переход на страницу.py') 
element=    browser.find_element_by_id("file") 
element.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()

