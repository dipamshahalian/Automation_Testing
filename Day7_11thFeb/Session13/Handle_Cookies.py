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
driver.get("https://demo.nopcommerce.com/")

# Maximize window
driver.maximize_window()

# No. fo Cookies:
cookies = driver.get_cookies()
print("Size of cookies:", len(cookies))  # ✅ Correct way

# # Info of Cookies
# for c in cookies:
#     # print(c) # Now if I want some specific info of cookies only instead of whole dictionary
#     print(c.get('name'), ":", c.get('value'))

# Now wanna make own cookies
# driver.add_cookie({"name":"Dipam1", "value":"1010"}) # for that we specify it in dictionary
#
# #  Now again count the cookies
# cookies = driver.get_cookies()
# print("Size of cookies updated:", len(cookies))  # ✅ Correct way
#
# # Now wanna delete a specific cookie
# driver.delete_cookie("Dipam1")
# cookies = driver.get_cookies()
# print("Size of cookies updated:", len(cookies))  # ✅ Correct way

# Now deleting all the cookies
driver.delete_all_cookies()

cookies = driver.get_cookies()
print("Size of cookies:", len(cookies))  # ✅ Correct way







time.sleep(3600)

# Close the browser
driver.quit()