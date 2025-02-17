from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Login Page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Maximize the window
driver.maximize_window()

# Wait for the login page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "username")))

# Perform Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for Dashboard to Load
wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

# Navigate to System Users Page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

# Wait for the user table to be visible
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']")))

# Get all rows in the table
rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")

# Count total rows
total_rows = len(rows)
print(f"Total Users Found: {total_rows}")

# Variables to count Enabled & Disabled users
enabled_count = 0
disabled_count = 0

# Loop through each row and get the "Status" column (5th column)
for r in range(1, total_rows + 1):
    status_xpath = f"(//div[@class='oxd-table-body']/div[{r}]/div/div[5])"

    # Wait for status element to be visible
    try:
        status_element = wait.until(EC.presence_of_element_located((By.XPATH, status_xpath)))
        status = status_element.text.strip()  # Get text and remove extra spaces

        # Count Enabled and Disabled users
        if status.lower() == "enabled":
            enabled_count += 1
        elif status.lower() == "disabled":
            disabled_count += 1
    except:
        print(f"⚠️ Could not find status for row {r}")

# Print the counts
print(f"Total Enabled Users: {enabled_count}")
print(f"Total Disabled Users: {disabled_count}")

# Close browser
driver.quit()
