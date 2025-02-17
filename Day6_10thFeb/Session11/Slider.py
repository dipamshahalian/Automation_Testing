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
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

# Maximize window
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']//span[2]")

# for fnding location we use location() method
print("Location of Sliders before moving: ")
print(min_slider.location) #    {'x': 59, 'y': 250}
print(max_slider.location) #    {'x': 766, 'y': 250}

#We cant't change in Y-axis, we can only move in the X direction

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 169, 0).perform()
act.drag_and_drop_by_offset(max_slider, -200, 0).perform()

print("Location of Sliders after moving: ")
print(min_slider.location)
print(max_slider.location)



time.sleep(3600)

# Close the browser
driver.quit()