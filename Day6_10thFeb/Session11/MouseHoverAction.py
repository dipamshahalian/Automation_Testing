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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Maximize window
driver.maximize_window()
time.sleep(3)


MouseHover_btn = driver.find_element(By.XPATH, "//button[@id='mousehover']")
Top = driver.find_element(By.XPATH, "//a[normalize-space()='Top']")
Reload = driver.find_element(By.XPATH, "//a[normalize-space()='Reload']")


# MouseHover

act = ActionChains(driver)  #Here it is required to pass the Driver instance in the ActionChains() otherwise it won't wrk

act.move_to_element(MouseHover_btn).move_to_element(Top).move_to_element(Reload).click().perform() # First hover thats why move to then click nd then perform is mandatory






time.sleep(3600)

# Close the browser
driver.quit()