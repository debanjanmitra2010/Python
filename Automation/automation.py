from selenium import webdriver
import time

chrome_browser = webdriver.Chrome("Automation/chromedriver.exe")
chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

time.sleep(4)

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title

chrome_browser.find_element_by_link_text('No, thanks!').click()

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM DEBANJAN MITRA')

time.sleep(2)

button = chrome_browser.find_element_by_css_selector('#get-input .btn')
button.click()

sum1 = chrome_browser.find_element_by_id('sum1')
sum1.clear()
sum1.send_keys('7')

sum2 = chrome_browser.find_element_by_id('sum2')
sum2.clear()
sum2.send_keys('5')

time.sleep(2)

button = chrome_browser.find_element_by_css_selector('#gettotal .btn')
button.click()

chrome_browser.quit()
