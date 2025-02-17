# %%
# Import necessary libraries
# from telnetlib import EC

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
driver = webdriver.Chrome(service=webdriver_service,
options=chrome_options)

# test open google website
driver.get('https://www.google.com')
time.sleep(5)

#navigate to login gmail
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")
driver.maximize_window()

# Identify the user name text box and enter the value
driver.find_element(By.ID,
"identifierId").send_keys("riap1330@gmail.com")
time.sleep(2)

# Clicks on the 'Next' button and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

driver.find_element(By.XPATH,
'//input[@name="Passwd"]').send_keys("Abc@556466")
time.sleep(2)

# Clicks on the 'Next' button again and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Searchmail']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Searchmail']").send_keys("Alian Hub have sent you an invitation")
time.sleep(1)

# Press Enter
driver.find_element(By.XPATH, "//input[@placeholder='Searchmail']").send_keys(Keys.ENTER)
time.sleep(1)

# first_email = driver.find_element(By.CSS_SELECTOR,"tr.zA:nth-of-type(1)")
# first_email.click()

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(2)  # Wait for Gmail to load more emails

time.sleep(2)

driver.get("https://mail.google.com/mail/u/0/#search/Alian+Hub+have+sent+you+an+invitation/FMfcgzQZTCjfmHsFnRfxBwKfXvkzsDNq")

time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Click here toJoin']").click()


# Wait for the new tab to open
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

# Now you can perform actions on the new tab
print("Switched to child window:", driver.title)

time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Create anAccount']").click()

# NOW ADDING USER DETAILS

driver.implicitly_wait(5)
driver.find_element(By.ID,"firstName").send_keys("Dipam")
driver.find_element(By.ID,"lastName").send_keys("Shah")
driver.find_element(By.XPATH,
"//input[@id='inputId']").send_keys("dipam.shah@aliansoftware.com")
driver.find_element(By.ID,"password").send_keys("Dipam@223133")
driver.find_element(By.ID,"confirmPassword").send_keys("Dipam@223133")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button").click()

time.sleep(2)
driver.get("https://mail.aliansoftware.com:2096/cpsess5398813076/3rdparty/roundcube/index.php?_task=mail&_mbox=INBOX")

# Wait for the second child window to open
time.sleep(3)  # Use explicit waits in real scripts

# Store the first child window handle
first_child_window = driver.current_window_handle

# Get the updated list of window handles
window_handles = driver.window_handles

# Switch to the second child window
for handle in window_handles:
     if handle != parent_window and handle != first_child_window:
         driver.switch_to.window(handle)
         break

# Now you are in the second child window
print("Switched to second child window:", driver.title)





time.sleep(3)
print("Test case passed")




time.sleep(3600)
#Uncomment below code to close the browser
#driver.close()