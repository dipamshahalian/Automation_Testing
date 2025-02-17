from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()

# Click the "Make Appointment" button
driver.find_element(By.ID, "btn-make-appointment").click()

# Wait for the page to load
time.sleep(3)

# Verify URL changed
assert driver.current_url != "https://katalon-demo-cura.herokuapp.com/", "Failed: URL did not change"

# Enter username and password
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")

# Click the Login button
driver.find_element(By.ID, "btn-login").click()

# Wait for the next page to load
time.sleep(3)

# Verify we reached the appointment page
expected_url = "https://katalon-demo-cura.herokuapp.com/#appointment"
assert driver.current_url == expected_url, "Failed: Incorrect page"

# Verify "Make Appointment" text is present
assert "Make Appointment" in driver.page_source, "Failed: Text not found"

print("Test Passed: Make Appointment flow verified successfully!")

# Close the browser
driver.quit()
