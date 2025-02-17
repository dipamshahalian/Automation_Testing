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

# Open the OrangeHRM login page
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #to maximize the browser window

time.sleep(3)

# ID and NAME locators
# driver.find_element(By.ID,"small-searchterms").send_keys("Apple iPhone 15 128GB") # ID
# similarly By.NAME

# LINK_TEXT and PARTIAL_LINK_TEXT
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.LINK_TEXT,"Reg").click()


# Class LOCATOR



time.sleep(3600)
driver.quit()