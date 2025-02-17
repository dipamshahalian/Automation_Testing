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
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")

#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/self::a").text
# print(text_msg)


# parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/parent::td").text
# print(text_msg)

# child
# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/child::td") # Switching from self node to the Ancestor node and then again to child node.
# print(len(childs))


# In single web element we can capture the text bt not in others like child above ex. cuz of multiple elements


# ancestor
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr").text
# print(text_msg)

# descendant
# descendants = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/descendant::*")
# print("No. of descendants found: ",len(descendants))

# following
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/following::*")
# print("No. of following elements found: ",len(following))

# following-sibling
# followingsiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/following-sibling::*")
# print("No. of following siblings found: ",len(followingsiblings))

# following siblings with specific requirement like only the ones with tr tag then jst change * into tr
# followingsiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/following-sibling::tr")
# print("No. of following siblings having tr tag found: ",len(followingsiblings))


# siblings
# precedings = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/preceding::*")
# print(len(precedings))

# preceding-sibling
precedings_siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'GPT Infraprojects')]/ancestor::tr/preceding-sibling::*")
print(len(precedings_siblings))





# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()
