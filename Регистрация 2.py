from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
required_elements = browser.find_elements_by_css_selector('input[required]')
for element in required_elements:
    element.send_keys('required')
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)

