from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://demo.nopcommerce.com/")

# Maximize window
driver.maximize_window()

# driver.save_screenshot("C:/Users/Alian-172/Desktop/Automation_Testing/Automation_Testing-master/Day7_11thFeb/Session14/homepage.png")
# driver.save_screenshot(os.getcwd()+"homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"ss.png")

# to hv ss in Binary or ASCII form:
# driver.get_screenshot_as_png() or
# driver.get_screenshot_as_base64()




time.sleep(3600)

# Close the browser
driver.quit()