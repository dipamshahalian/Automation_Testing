from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"


# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Facebook Signup Page
driver.get("https://www.facebook.com/reg/")

# Wait for the 'Month' dropdown to be visible
month_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "month"))
)

# Create Select object
select_month = Select(month_dropdown)

# Print the default selected month
print("Default Selected Month:", select_month.first_selected_option.text)

# Select a different month
# select_month.select_by_visible_text("Dec") #using the exact text
# select_month.select_by_index(9) #using index no.
select_month.select_by_value("6") #By using the value

# capture all the opts and print them
all_options = select_month.options
print("Total no. of options:", len(all_options)) #len

# actual text written:
# for i in all_options:
#     print(i.text)

# NOW TO SELECT THE OPTION WITHOUT USING ANY BUILT-IN METHOD

# for i in all_options:
#     if i.text=="Oct":
#         i.click()
#         break

# To print no. of opts.
# Locate the dropdown and create a Select object
select_month = Select(driver.find_element(By.XPATH, "//select[@id='month']"))

# Get the length of the options in the dropdown
print(len(select_month.options))



# Verify new selection
# print("After Selection:", select_month.first_selected_option.text)

time.sleep(3600)  # Pause for observation
driver.quit()
