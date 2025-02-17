import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

try:
    wait = WebDriverWait(driver, 10)

    # Scroll down to make the date picker visible
    driver.execute_script("window.scrollBy(0, 500);")

    # Open the date picker
    date_input = wait.until(EC.element_to_be_clickable((By.ID, "dob")))
    date_input.click()

    # ✅ Set your target past date (modify this)
    target_year = "2021"
    target_month = "March"
    target_date = "5"

    # ✅ Prevent infinite loop (max 30 attempts)
    max_attempts = 30
    attempts = 0

    while attempts < max_attempts:
        time.sleep(1)  # Allow UI to update

        # ✅ Get current month and year from the date picker
        current_month = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-month"))).text.strip()
        current_year = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-year"))).text.strip()

        print(f"📅 Current: {current_month} {current_year} | Target: {target_month} {target_year}")

        # ✅ Stop once the correct month & year are reached
        if current_month == target_month and current_year == target_year:
            break

        # ✅ Click the "Previous" button to go backward
        prev_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ui-icon-circle-triangle-w")))
        prev_button.click()
        attempts += 1

    if attempts == max_attempts:
        print("⚠️ Max attempts reached! Check the target date.")

    # ✅ Select the target date
    date_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody//tr/td/a")))

    for date_element in date_elements:
        if date_element.text.strip() == target_date:
            date_element.click()
            print(f"✅ Date {target_date} selected!")
            break

    time.sleep(5)  # Just to see the selected date

finally:
    driver.quit()  # Close browser
