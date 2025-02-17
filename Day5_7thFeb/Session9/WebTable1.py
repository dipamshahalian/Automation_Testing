# 1. Count no. of rows and columns
# 2. Read specific row and col data
# 3. Read all the rows and cols data
# 4. Read data base on the conditions ( e.x. read data whose author is MUkesh)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# So now onwards no need to specify the whole path cuz selenium takes it by its own

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL
driver.get("https://testautomationpractice.blogspot.com/")

# Operations to be Performed

# 1. Count no. of rows and columns
# print("No. of Rows:", len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))) #for this I had modified the XPATH to calculate total tr
# print("No. of Columns:", len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))) #for this I had modified the XPATH to calculate total th

# 2. Read specific row and col data
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)

# 3. Read all the rows and cols data
# print("Printing all rows and col.s data:\n")
# for r in range(2, 8):
#     for c in range(1,5):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text # Here we make our XPATH dynamic bt specifying the r and c as string and putting em in the double quotation
#         # print(data)
#         print(data, end="  ") #Now if I wanna print in the form as it is then use this
#     print()

# 4. Read data base on the conditions ( e.x. read data whose author is MUkesh)
print("Books written by Mukesh:")
for r in range(2, 8):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text.strip()

    if authorName == "Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text.strip() # To print the Book Name
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text.strip() # To print the Price
        print(bookname, "  ", authorName, " ", price)




# Maximize window
driver.maximize_window()

time.sleep(3600)

# Close the browser
driver.quit()