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
# driver.get("https://the-internet.herokuapp.com/basic_auth") #But here we can't do anything with such URL
# So Bypassing it
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")




# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()