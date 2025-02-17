from dataclasses import field

from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

# Maximize window
driver.maximize_window()


driver.switch_to.frame("iframeResult") # Switch to the frame

field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear() #Adding this cuz some text is already written in that field
field1.send_keys("Dipam")

btn = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(btn).perform() # double click action











time.sleep(3600)

# Close the browser
driver.quit()