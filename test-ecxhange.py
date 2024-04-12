import xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.twse.com.tw/zh/index.html"
driver.get(url)

element = driver.find_element(By.XPATH, xpath.transaction_info_btn)
element.click()
time.sleep(2)
element = driver.find_element(By.XPATH, xpath.stock_price_and_mothly_btn)
element.click()
time.sleep(2)
element = driver.find_element(By.XPATH, xpath.year_112_selector_option)
element.click()
element = driver.find_element(By.XPATH, xpath.month_selector)
element.click()
element = driver.find_element(By.XPATH, xpath.stock_number_input)
element.send_keys("2330")
element = driver.find_element(By.XPATH, xpath.search_btn)
element.click()
time.sleep(2)
required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(required_width, required_height)
time.sleep(2)
full_page = driver.find_element(By.TAG_NAME, "body")
full_page.screenshot("screenshot.png")
table_content = driver.find_elements(By.XPATH, xpath.table)
for i in range(1, len(table_content)):
    element = driver.find_element(By.XPATH, xpath.table_content.format(i=i))
    print(element.text)

driver.quit()
