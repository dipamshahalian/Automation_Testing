from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://mail.google.com/mail/u/0/#inbox")

# Clicking the acc
driver.find_element(By.XPATH, "//input[@id='identifierId']").send_keys("riap1330@gmail.com")

time.sleep(3)

driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()