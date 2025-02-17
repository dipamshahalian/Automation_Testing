from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/login")
time.sleep(3)
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/signup")

# back(), forward() and refresh()
# driver.back()
# driver.forward()
driver.refresh()

# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()