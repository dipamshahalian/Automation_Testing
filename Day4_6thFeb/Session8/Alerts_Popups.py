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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)

# Since Alert is not a webel therefore we use switch
alertwindow = driver.switch_to.alert
print(alertwindow.text)

# Now passing a msg i.e. value to the alert box
alertwindow.send_keys("Yo Dipam here")

# Now to close the alert window (we hv two opts either by OK or Cancel)
# alertwindow.accept() #For OK button

alertwindow.dismiss() #Now using Cancel Button


# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()