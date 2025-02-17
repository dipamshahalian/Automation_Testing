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
driver.get("https://usersnap.com/blog/long-scrolling-websites-tips-best-practices/")

# Maximize window
driver.maximize_window()

# 3 approaches
# (Remember that scrolling is done through the web browser and JS is used in it)


# 1 Scroll using pixel no.s

# driver.execute_script("window.scrollBy(0, 3000)", "") # By using this we can pass some JS statements
# value = driver.execute_script("return window.pageYOffset;") # It will return the exact value of pixels moved
# print("No. of px moved", value)

# 2 Scroll till the element is visible

# ele = driver.find_element(By.XPATH, "//strong[normalize-space()='Structuring Content Appropriately']")
# driver.execute_script("arguments[0].scrollIntoView();", ele)
# value = driver.execute_script("return window.pageYOffset;")
# print("No. of px moved", value)

# 3 Scroll the page till the end

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(5)
# Now If I wanna come back at the top i.e. original postion of scroll bar then
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")



time.sleep(3600)

# Close the browser
driver.quit()