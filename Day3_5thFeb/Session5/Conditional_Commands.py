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
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/login?redirect_url=/")

# is_displayed()
email_id = driver.find_element(By.XPATH,"//input[@id='email']")
print("Display Status", email_id.is_displayed())

# is_enabled()
print("Enabled Status", email_id.is_enabled())

# is_selected()
remember_checkbox = driver.find_element(By.XPATH, "//label[@for='chk-remember-me']")
print("Is selected?", remember_checkbox.is_selected())

# now checking it and then again checking the status:
# remember_checkbox.click()
# print("Is selected?", remember_checkbox.is_selected())

# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()
