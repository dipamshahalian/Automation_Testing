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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# Maximize window
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()


countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries_list))

for country in countries_list:
    if country.text == "Monaco":
        country.click()
        break


time.sleep(3600)

# Close the browser
driver.quit()