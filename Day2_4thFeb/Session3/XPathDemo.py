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
driver.get("https://automationbookstore.dev/")

# Maximize window
driver.maximize_window()

# Absolute Xpath

# driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/form[1]/div[1]/input[1]').send_keys('Test')
# driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/ul[1]/li[3]/a[1]/p[1]').click()

# Relative Xpath
# Relative Xpath
# driver.find_element(By.XPATH,"//input[@id='searchBar']").send_keys('Test')  # Fixed XPath for search input field
# driver.find_element(By.XPATH,"//h2[@id='pid3_title']").click()

# Using Operators
# 1) or
# driver.find_element(By.XPATH,"//input [@id='searchBar' or @class='ui-focus']").send_keys('Test')

# 2) and
# driver.find_element(By.XPATH, "//input[@id='searchBar' and @class='ui-focus']").send_keys('Test')

# 3) contains()
# driver.find_element(By.XPATH,"//input[contains(@id,'searchBar')]").send_keys('Test')
# driver.find_element(By.XPATH,"").click()

# 4) starts-with()
# driver.find_element(By.XPATH," //input[starts-with(@class,'ui')]").send_keys('Test')

# 5) text()
driver.find_element(By.XPATH,"//h1[text()='Automation Bookstore']").is_selected()



time.sleep(3600)

# Close the browser
driver.quit()