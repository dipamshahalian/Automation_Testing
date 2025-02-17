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

# Open the AlianHub login page
driver.get("https://app.alianhub.com/#/login?redirect_url=/6571e7165470e64b12032734/project/6571e7195470e64b1203295e/fs/661d3cebfbfc309e21909648/6774d7302696c538efc86efd/679af1602a3d7720627e4bf7?tab=ProjectListView%26detailTab=task-detail-tab")

# Maximize window
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Enter Email
driver.find_element(By.ID, "email").send_keys("dipam.shah@aliansoftware.com")

# Enter Password
driver.find_element(By.ID, "password").send_keys("Dipam@223133")

# Click the Login Button (Using XPath for better accuracy)
driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-login')]").click()

# Wait for redirection to the dashboard
time.sleep(5)

# Capture and print the current page title (for verification)
act_title = driver.title
print(f"Current Page Title: {act_title}")

# Keep the browser open for manual verification
time.sleep(3600)

# Close the browser
driver.quit()
