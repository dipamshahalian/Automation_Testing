from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open Gmail login page
driver.get("https://accounts.google.com/v3/signin/identifier?service=mail")
wait = WebDriverWait(driver, 10)

# Enter Email
email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_input.send_keys("riap1330@gmail.com")
driver.find_element(By.XPATH, "//span[text()='Next']").click()

# Wait and enter password
password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
password_input.send_keys("Abc@556466")
driver.find_element(By.XPATH, "//span[text()='Next']").click()

# Wait for search box to appear
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search mail']")))
search_box.send_keys("Alian Hub have sent you an invitation")
search_box.send_keys(Keys.ENTER)

# Wait for first email and click
first_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@role='grid']//tr[contains(@class, 'zA')][1]")))
first_email.click()

# Wait to observe (or process the email)
time.sleep(10)

# Uncomment this to close the browser
# driver.quit()
