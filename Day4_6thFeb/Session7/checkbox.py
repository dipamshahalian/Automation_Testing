from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Maximize window to avoid layout issues
driver.maximize_window()

# Open URL
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
wait = WebDriverWait(driver, 10)

# Remove iframes (ads) that may block interaction
driver.execute_script("document.querySelectorAll('iframe').forEach(iframe => iframe.remove());")

# Locate all checkboxes with 'profession' in their name
multiple_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@name,'profession')]")
print(len(multiple_checkboxes))

# Scroll into view and click checkboxes safely
for checkbox in multiple_checkboxes:
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)  # Bring into view
    time.sleep(1)  # Small delay to ensure visibility
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkbox)).click()
    except:
        driver.execute_script("arguments[0].click();", checkbox)  # Fallback JS click

# Delay to observe selected checkboxes
time.sleep(10)

# Clearing all selected checkboxes
for checkbox in multiple_checkboxes:
    if checkbox.is_selected():
        driver.execute_script("arguments[0].click();", checkbox)  # Ensure click works

# Keep the browser open for observation
time.sleep(3600)

# Close the browser
driver.quit()
