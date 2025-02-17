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
# wait = WebDriverWait(driver, 10)

# Open URL
driver.get("https://aliansoftware.com/")
wait = WebDriverWait(driver, 10)

# Handling Links
# driver.find_element(By.LINK_TEXT,"View All").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Node").click()

# Find no. of links in a webpage
links = driver.find_elements(By.TAG_NAME, "a")
# can  also be done using XPAT \\a

print("total no. of linkls", len(links))

# Now wanna kw the name of all the links
# so for that we use for loop

for link in links:
    print(link.text)
#  Some empty space in o/p sows that text is not present for that links




# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()