from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the website with an iframe
    driver.get("https://jqueryui.com/droppable/")

    # Maximize window
    driver.maximize_window()

    # Wait for the iframe to load and switch to it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    # Locate the draggable and droppable elements
    draggable = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    droppable = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

    # Perform drag and drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()

    # Verify the drop was successful by checking the new text
    dropped_text = droppable.text
    print("Dropped Box Text:", dropped_text)  # Expected: "Dropped!"

    # Switch back to the main page
    driver.switch_to.default_content()

    # Print confirmation from the main page
    main_heading = driver.find_element(By.TAG_NAME, "h1").text
    print("Main Page Heading:", main_heading)  # Expected: "Droppable"

    # Wait to observe result
    time.sleep(5)

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
