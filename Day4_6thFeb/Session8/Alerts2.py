from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)


# Open URL
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)
driver.switch_to.alert.accept()




# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()