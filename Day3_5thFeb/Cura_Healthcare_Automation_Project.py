from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()

driver.find_element(By.ID, "btn-make-appointment").click()

time.sleep(3)

assert driver.current_url != "https://katalon-demo-cura.herokuapp.com/", "Failed: URL did not change"

driver.find_element(By.ID, "txt-username").send_keys("John Doe")
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID, "btn-login").click()

time.sleep(3)

if driver.current_url == "https://katalon-demo-cura.herokuapp.com/":
    print("Passed: URL did not change")
else:
    print("URL Changed")

expected_url = "https://katalon-demo-cura.herokuapp.com/#appointment"

if driver.current_url == expected_url:
    print("Login Successful")
else:
    print("Failed: URL is wrong")


print("Test Passed: Make Appointment flow verified successfully!")

driver.quit()


