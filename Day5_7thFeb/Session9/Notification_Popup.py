from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications") # To disable the notifications i.e. clicking that cross btn X so that we can proceed to the webpage

chrome_driver_path = "C:/Users/Alian-172/Desktop/Automation_Testing/Automation_Testing-master/chromedriver-win64/chromedriver-win64"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=ops)

# Open URL
driver.get("https://whatmylocation.com/")

# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()