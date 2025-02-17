from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# mywait = WebDriverWait(driver, 10) #Explicit Wait Declaration # Its still a basic one so the modified one:
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception]) # poll_frequency makes it faster by checking the condition in defined no. of times.

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

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Hire graphic designer: A guide to selecting an exp')]"))) # Using explicit wait
searchlink.click()


time.sleep(100)  # Adjust this wait based on page loading time

# Close the browser
driver.quit()
