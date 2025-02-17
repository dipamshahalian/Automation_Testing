from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Define the path to chromedriver.exe
chrome_driver_path = "/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up the Chrome service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the window
driver.maximize_window()

# Wait for elements to load
time.sleep(3)

# Enter Username
username_field = driver.find_element(By.NAME, "username")
username_field.clear()
username_field.send_keys("Admin")

# Enter Password
password_field = driver.find_element(By.NAME, "password")
password_field.clear()
password_field.send_keys("admin123")

# Click Login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the homepage to load
time.sleep(5)

# Capture and verify the title of the homepage
act_title = driver.title  # Actual Title
exp_title = "OrangeHRM"   # Expected Title

if act_title == exp_title:
    print("Login test passed!")
else:
    print("Login test failed!")

# Keep the browser open for manual verification
time.sleep(3600)  # Change this if you want it to close sooner

# Close the browser
driver.quit()
