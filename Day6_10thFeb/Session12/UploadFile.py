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
driver.get("https://practice.expandtesting.com/upload#google_vignette")

# Maximize window
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='fileInput']").send_keys("C:/Users/Alian-172/Desktop/Automation_Testing/Automation_Testing-master/Day6_10thFeb/Session12/test.pdf")







time.sleep(3600)

# Close the browser
driver.quit()