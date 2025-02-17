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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# Maximize window
driver.maximize_window()

time.sleep(2)

btn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(btn).perform()   # right click method

driver.find_element(By.XPATH, "/html/body/ul/li[3]").click()
time.sleep(5)
driver.switch_to.alert.accept()




time.sleep(3600)

# Close the browser
driver.quit()