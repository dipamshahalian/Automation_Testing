from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up the Chrome service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)
driver.get("https://automationbookstore.dev/")
driver.maximize_window()

# CLASS_NAME locator
sliders = driver.find_elements(By.CLASS_NAME, 'ui-li-has-thumb')
print(len(sliders)) # 8 is the o/p

# Now to kw abt the Total no. of a tags present
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links)) # total no. of links: 9

time.sleep(3600)
driver.quit()