from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

# Maximize window
driver.maximize_window()

# Wait for elements to be present
wait = WebDriverWait(driver, 10)

# ✅ Corrected Locator - Use ID directly instead of XPath
source = wait.until(EC.presence_of_element_located((By.ID, "box6")))
target = wait.until(EC.presence_of_element_located((By.ID, "box103")))

# Perform drag-and-drop action
act = ActionChains(driver)
act.drag_and_drop(source, target).perform()

# Keep the browser open for user interaction
input("Press Enter to exit...")

# Close the browser
driver.quit()
