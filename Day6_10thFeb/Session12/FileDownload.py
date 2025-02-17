import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Get current working directory
location = os.getcwd()

# ---------------------------- Chrome

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    # Automatically manage ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Set download preferences
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()  # Correctly initialize options
    ops.add_experimental_option("prefs", preferences)

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=ops)

    return driver  # Return driver instance


# ---------------------------- Edge

def edge_setup():
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    # Automatically manage EdgeDriver
    service = Service(EdgeChromiumDriverManager().install())

    # Set download preferences
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()  # Use EdgeOptions for Edge
    ops.add_experimental_option("prefs", preferences)

    # Initialize WebDriver
    driver = webdriver.Edge(service=service, options=ops)

    return driver  # Return driver instance


# ---------------------------- Firefox

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager

    # Automatically manage GeckoDriver for Firefox
    service = Service(GeckoDriverManager().install())

    # Set download preferences for Firefox
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.download.folderList", 2)  # Use custom download location
    ops.set_preference("browser.download.dir", location)  # Set the dynamic download path
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # Skip download pop-up

    # Initialize WebDriver
    driver = webdriver.Firefox(service=service, options=ops)

    return driver  # Return driver instance



# ---------------------------- Running the script with different browsers

# Uncomment the desired browser to test:

# Chrome
# driver = chrome_setup()

# Edge
# driver = edge_setup()

# Firefox
driver = firefox_setup()

# Open the website
driver.get("https://practice-automation.com/file-download/")
driver.maximize_window()

time.sleep(3)

# Click the file download button
driver.find_element(By.XPATH, "//*[@id='post-1042']/div/div[1]/div/div/div/div[3]/a").click()

time.sleep(3)  # Wait for the download to complete

# Keep browser open for verification
time.sleep(100)
