import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Dipam@223133",
    database="mydb"
)

curs = con.cursor()

# Select all students
curs.execute("SELECT * FROM student")
all_students = curs.fetchall()
print("All Students:")
for student in all_students:
    print(student)

# Fetch only Lewis Hamilton's record
curs.execute("SELECT * FROM student WHERE first_name = 'Lewis' AND last_name = 'Hamilton'")
lewis = curs.fetchone()
print("\nLewis Hamilton's Record:")
print(lewis)

# Close the connection
curs.close()
con.close()

import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Dipam@223133",
    database="mydb"
)

curs = con.cursor()

#  Fetch driver data
curs.execute("SELECT first_name, last_name, email FROM f1_drivers")
drivers = curs.fetchall()

#  Set up Selenium WebDriver (Example: Chrome)
driver = webdriver.Chrome()

#  Iterate through database records
for driver_data in drivers:
    first_name, last_name, email = driver_data
    print(f"Testing login for: {first_name} {last_name} - {email}")

    driver.get("https://example.com/login")
    time.sleep(2)

    #  Locate fields & perform actions
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys("Test@123")  # Sample password
    driver.find_element(By.ID, "loginButton").click()

    time.sleep(3)  # Wait for login response

    #  Add validation (Example: Check if login was successful)
    if "dashboard" in driver.current_url:  # Replace with actual dashboard URL
        print(f" Login successful for {first_name} {last_name}")
    else:
        print(f" Login failed for {first_name} {last_name}")

#  Close browser & DB connection
driver.quit()
curs.close()
con.close()
