# Chrome


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
#
#
# def headless_chrome():
#     # Automatically manage ChromeDriver
#     service = Service(ChromeDriverManager().install())
#
#     # Set Chrome options
#     ops = Options()
#     ops.add_argument("--headless=new")  # ✅ Correct way for headless mode
#     ops.add_argument("--disable-gpu")  # ✅ Prevents GPU-related crashes in headless mode
#     ops.add_argument("--window-size=1920,1080")  # ✅ Ensures correct rendering
#     ops.add_argument("start-maximized")  # ✅ Maximizes window
#     ops.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")  # ✅ Helps bypass bot detection
#
#     # Initialize WebDriver
#     driver = webdriver.Chrome(service=service, options=ops)
#     return driver
#
#
# # Start headless browser
# driver = headless_chrome()
# driver.get("https://demo.nopcommerce.com/")
#
# # Wait to ensure page loads properly (if necessary)
# driver.implicitly_wait(5)
#
# # Print page details
# print("Title:", driver.title)  # ✅ Prints the title correctly
# print("URL:", driver.current_url)  # ✅ Prints the correct URL
#
# # Close the browser
# driver.quit()



# -----------------Edge
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.edge.options import Options
#
# def headless_edge():
#     # Automatically manage Edge WebDriver
#     service = Service(EdgeChromiumDriverManager().install())
#
#     # Set Edge options
#     ops = Options()
#     ops.add_argument("--headless=new")  # ✅ Headless mode for Edge
#     ops.add_argument("--disable-gpu")
#     ops.add_argument("--window-size=1920,1080")
#     ops.add_argument("start-maximized")
#     ops.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#
#     # Initialize WebDriver
#     driver = webdriver.Edge(service=service, options=ops)
#     return driver
#
# # Start Edge in headless mode
# driver = headless_edge()
# driver.get("https://demo.nopcommerce.com/")
#
# # Print details
# print("Title:", driver.title)
# print("URL:", driver.current_url)
#
# # Close browser
# driver.quit()




# --------------Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def headless_firefox():
    # Automatically manage Firefox WebDriver
    service = Service(GeckoDriverManager().install())

    # Set Firefox options
    ops = Options()
    ops.add_argument("--headless")  # ✅ Headless mode for Firefox
    ops.add_argument("--disable-gpu")
    ops.add_argument("--window-size=1920,1080")
    ops.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    # Initialize WebDriver
    driver = webdriver.Firefox(service=service, options=ops)
    return driver

# Start Firefox in headless mode
driver = headless_firefox()
driver.get("https://demo.nopcommerce.com/")

# Print details
print("Title:", driver.title)
print("URL:", driver.current_url)

# Close browser
driver.quit()

