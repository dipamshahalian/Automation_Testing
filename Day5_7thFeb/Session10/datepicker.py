import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

try:
    # Switch to the datepicker frame
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    # Open the date picker
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "datepicker"))).click()

    # Target date
    target_month, target_year, target_date = "October", "2023", "10"

    # Loop to navigate to the correct month/year
    while True:
        current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        if current_month == target_month and current_year == target_year:
            break  # Stop if the correct month/year is found

        # Click the next button
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ui-icon-circle-triangle-e"))).click() # Similarly can do for the previous date button

    # Select the date
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{target_date}']"))).click()

    # Select date
    # dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody//tr/td/a")
    # for date in dates:
    #     if date.text == target_date:
    #         date.click()
    #         break





    # Keep the browser open for a while to observe the result
    time.sleep(5)

finally:
    # Ensure the browser closes after execution
    driver.quit()
