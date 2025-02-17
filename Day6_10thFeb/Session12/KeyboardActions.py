from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Correct import
import time

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://text-compare.com/")
driver.implicitly_wait(10)

# Maximize window
driver.maximize_window()

# Locate input fields
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

# Type text
input1.send_keys("Hey this is Dipam Shah")

# Initialize ActionChains
act = ActionChains(driver)

# Select text using Ctrl + A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#  Now Copy the text i.e. Ctrl+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Now pressing the Tab Key to navigate to the second
act.send_keys(Keys.TAB).perform()

# Now pasting i.e. Ctrl+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()



# Pause for testing (change to a smaller sleep duration if needed)
time.sleep(10)

# Close the browser
driver.quit()
