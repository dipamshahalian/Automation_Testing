from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options to
    #Disable the "enable-automation" flag.
    #Add the "no-sandbox" argument.
    #Add the "disable-infobars" argument.
    #Add the "disable-dev-shm-usage" argument.

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set the driver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# test open google website
driver.get('https://www.google.com')
time.sleep(5)

#navigate to login gmail
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")
driver.maximize_window()

# Identify the user name text box and enter the value
driver.find_element(By.ID, "identifierId").send_keys("riap1330@gmail.com")
time.sleep(2)

# Clicks on the 'Next' button and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("Abc@556466")
time.sleep(2)

# Clicks on the 'Next' button again and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Search mail']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Search mail']").send_keys("Alian Hub have sent you an invitation")
time.sleep(1)

# Press Enter
driver.find_element(By.XPATH, "//input[@placeholder='Search mail']").send_keys(Keys.ENTER)
time.sleep(1)

time.sleep(2)

driver.find_element(By.XPATH,"//tr[contains(@class, 'zA')]/td[6]/div/div/div[2]").click()

time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[href*='alianhub-beta']").click()


driver.implicitly_wait(5)

time.sleep(3)  # Use explicit wait in real scripts

# Store parent window handle
parent_window = driver.current_window_handle

# Get all window handles
window_handles = driver.window_handles

# Switch to the new tab (child window)
for handle in window_handles:
     if handle != parent_window:
         driver.switch_to.window(handle)
         break

time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Create an Account']").click()
time.sleep(2)
driver.find_element(By.ID, "firstName").send_keys("Dipam")
driver.find_element(By.ID, "lastName").send_keys("Shah")
driver.find_element(By.ID, "inputId").send_keys("riap1330+105@gmail.com")
driver.find_element(By.ID, "password").send_keys("Abc@223133")
driver.find_element(By.ID, "confirmPassword").send_keys("Abc@223133")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button").click()

time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "//input[@id='email']").click()

driver.find_element(By.XPATH, "//input[@id='email']").send_keys("riap1330+105@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").click()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Abc@223133")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div/div/form/div[4]/button').click()







time.sleep(3)

time.sleep(3600)
