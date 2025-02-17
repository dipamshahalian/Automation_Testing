from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open URL
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Maximize window
    driver.maximize_window()

    # Wait for the frames to load
    wait = WebDriverWait(driver, 10)

    # Switch to the 'top' frame
    driver.switch_to.frame("frame-top")

    # Switch to the 'left' frame inside 'top'
    driver.switch_to.frame("frame-left")

    # Extract and print text inside the left frame
    left_text = driver.find_element(By.TAG_NAME, "body").text
    print("Left Frame Text:", left_text)

    # Switch back to 'top' frame
    driver.switch_to.parent_frame()

    # Switch to the 'middle' frame inside 'top'
    driver.switch_to.frame("frame-middle")

    # Extract and print text inside the middle frame
    middle_text = driver.find_element(By.ID, "content").text
    print("Middle Frame Text:", middle_text)

    # Switch back to 'top' frame
    driver.switch_to.parent_frame()

    # Switch to the 'right' frame inside 'top'
    driver.switch_to.frame("frame-right")

    # Extract and print text inside the right frame
    right_text = driver.find_element(By.TAG_NAME, "body").text
    print("Right Frame Text:", right_text)

    # Switch back to the main page
    driver.switch_to.default_content()

    # Switch to the 'bottom' frame
    driver.switch_to.frame("frame-bottom")

    # Extract and print text inside the bottom frame
    bottom_text = driver.find_element(By.TAG_NAME, "body").text
    print("Bottom Frame Text:", bottom_text)

    # Switch back to main content
    driver.switch_to.default_content()

except Exception as e:
    print("Error:", e)

finally:
    # Wait for a few seconds to see the result
    time.sleep(5)

    # Close the browser
    driver.quit()
