from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/Gmail related Chrome/chrome.exe"

# Initialize ChromeDriver with webdriver_manager to automatically manage driver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Gmail URL
driver.get("https://mail.google.com/mail/u/0/#inbox")

# Enter the email
driver.find_element(By.XPATH, "//input[@id='identifierId']").send_keys("riap1330@gmail.com")

time.sleep(3)

# Click 'Next'
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

# Maximize the browser window
driver.maximize_window()

# Wait for 1 hour (3600 seconds) or any duration you need
time.sleep(3600)

# Close the browser after the wait
driver.quit()
