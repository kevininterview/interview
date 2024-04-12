import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import xpath

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.twse.com.tw/zh/index.html"
driver.get(url)

def click_xpath(xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def input_xpath(xpath, value):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(value)

def screenshot():
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    time.sleep(2)
    full_page = driver.find_element(By.TAG_NAME, "body")
    full_page.screenshot("screenshot.png")

def print_stock_price():
    table_content = driver.find_elements(By.XPATH, xpath.table)
    for i in range(1, len(table_content)):
        element = driver.find_element(By.XPATH, xpath.table_content.format(i=i))
        print(element.text)


click_xpath(xpath.transaction_info_btn)
time.sleep(2)
click_xpath(xpath.stock_price_and_mothly_btn)
time.sleep(2)
click_xpath(xpath.year_112_selector_option)
click_xpath(xpath.month_selector)
input_xpath(xpath.stock_number_input, "2330")
click_xpath(xpath.search_btn)
screenshot()
print_stock_price()

driver.quit()
