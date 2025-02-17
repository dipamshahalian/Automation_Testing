from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
# driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/signup")

# --------find_element()

# scenario 1 Single Web Element
# element = driver.find_element(By.XPATH, "//input[@id='firstName']")
# element.send_keys("Dipam")

# scenario 2 Locator matching multiple web elements

# driver.get("https://aliansoftware.com/")
# element = driver.find_element(By.XPATH, "//footer[@id='main-footer']//a")
# print(element.text)

# scenario 3 NoSuchElementException.
# view_all = driver.find_element(By.LINK_TEXT, "View Al") # giving incorrect intentionally
# view_all.click()


# ----find_elements()

# driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/#/signup")

# scenario 1 Multiple Web Element
# elements = driver.find_elements(By.XPATH, "//input[@id='firstName']")
# print(len(elements))
# elements[0].send_keys("Alian") #Since its not possible to use send_keys in find_elements directly we do this step


# scenario 2 Locator matching multiple web elements

driver.get("https://aliansoftware.com/")
# elements = driver.find_elements(By.XPATH, "//footer[@id='main-footer']//a")
# print(len(elements))
# print(elements[0].text)
# Now If I wanna write name of multiple elements then I'll use loop

# for x in elements:
#     try:
#         print(x.text)
#     except Exception as e:
#         print(f"Skipping stale element: {e}")


# scenario 3 NoSuchElementException is not here.
elements = driver.find_elements(By.LINK_TEXT, "View Al") # giving incorrect intentionally
print("No. of elements returned:", len(elements))



# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()
