from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Define the path to chromedriver.exe
chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up the Chrome service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")
driver.maximize_window() #to maximize the browser window

# tag and id combination
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc") # tag name i.e here input is always optional
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc") # tag name i.e here input is always optional

# tag and class combination
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com") # tag name i.e here input is always optional

# tag and attribute combination
# driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("dipam@alian")

# tag class and attribute combination
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys("xyz")


time.sleep(3600)
driver.quit()