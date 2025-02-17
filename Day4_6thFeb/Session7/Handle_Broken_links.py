from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests as requests

# INSTALLED requests   PACKAGE WHICH IS MANDATORY FOR THIS

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("http://www.deadlinkcity.com/")

all_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url, " is a broken link")
        count+=1
    else:
        print(url, " is valid link")

print("Total broken links:", count)


# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()