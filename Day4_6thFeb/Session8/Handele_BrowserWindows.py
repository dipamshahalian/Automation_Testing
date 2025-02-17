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

# Open URL
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/signup")

# Maximize window
driver.maximize_window()

# Checking Window ID
# windowid = driver.current_window_handle
# print(windowid) #F991F1074C85637256CC41CBF3B6C465 Second time: 5CF54780B49540536F1B6B2B3A5E7951

# Opening multiple windows:
driver.find_element(By.LINK_TEXT, "Privacy Policy").click()
# Now I want window ID of multiple windows
windowsIDs = driver.window_handles

parentwindowid = windowsIDs[0]
childwindowid = windowsIDs[1]


# Approach 1
# print(parentwindowid, childwindowid

# driver.switch_to.window(childwindowid)
# print("title of child window", driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("title of parent window", driver.title)

# But if we have more no. of windows then we should do these approaches:

# Approach 2

# for windid in windowsIDs:
#     driver.switch_to.window(windid)
#     print(driver.title)

time.sleep(7)
for windid in windowsIDs:
    driver.switch_to.window(windid)
    if driver.title == "Alian Hub | Register" or driver.title == 'XYZ':
        driver.close()





time.sleep(3600)

# Close the browser
driver.quit()