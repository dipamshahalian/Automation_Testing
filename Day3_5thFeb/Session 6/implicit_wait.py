from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# Open URL
driver.get("https://aliansoftware.com/blogs/")

# Maximize window
driver.maximize_window()

# Introduce a wait to let the page load fully
time.sleep(2)

# Re-locate the search input field before interacting
search_input = driver.find_element(By.XPATH, "//input[@id='wp-block-search__input-1']")
search_input.send_keys("design")

# Re-locate again before submitting
search_input = driver.find_element(By.XPATH, "//input[@id='wp-block-search__input-1']")
search_input.submit()

# Now at a specific blog
a = driver.find_element(By.XPATH, "//h1[contains(text(),'Hire graphic designer: A guide to selecting an exp')]")
a.click()

time.sleep(100)  # Adjust this wait based on page loading time

# Close the browser
driver.quit()
