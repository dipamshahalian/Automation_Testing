from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Flipkart homepage
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()

"""
# Find the Login button
login_button = driver.find_element(By.XPATH, "//span[normalize-space()='Login']")

# Open the Login button link in a new tab using Right-Click + Open in New Tab (Ctrl + Click)
ActionChains(driver).key_down(Keys.CONTROL).click(login_button).key_up(Keys.CONTROL).perform()

# Sleep for observation
time.sleep(5)

# Switch to the new tab (optional, if you want to interact with it)
driver.switch_to.window(driver.window_handles[-1])

# Sleep for observation
time.sleep(10)
"""

# Now 2 tabs by get but opening them in diffn tabs

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(3)
# driver.switch_to.new_window('tab') #It opens in new tab
driver.switch_to.new_window('window')  #It opens in new window

driver.get("https://www.amazon.in/")


# Close the browser
driver.quit()
