from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_class_name("first")
input1.send_keys("Ivan")
input1 = browser.find_element_by_class_name("second")
input1.send_keys("Ivan")
input1 = browser.find_element_by_class_name("third")
input1.send_keys("Ivan")
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)
welcome_text_elt = browser.find_element_by_tag_name('h1')
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text