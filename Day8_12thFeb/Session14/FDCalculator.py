from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import XLUtils

chrome_driver_path = "C:/Users/001/Desktop/Automation_Testing/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Automatically manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

# Maximize window
driver.maximize_window()

file = "C:/Users/Alian-172/Downloads/caldata.xlsx"
rows  = XLUtils.getRowCount()

for r in range(2,rows+1):
    princi=XLUtils.readData(file,"Sheet1",r,1)
    roi=XLUtils.readData(file,"Sheet1",r,2)
    per1 = XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file,"Sheet1",r,4)
    frequency = XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue = XLUtils.readData(file,"Sheet1",r,6)
    # Passing data to application
    driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(principal)
    driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH,"//*[@id='tenure']").send_keys(per1)
    driver.find_element(By.XPATH, "//*[@id='frequency']").send_keys(per2)
    periodMenu = Select(driver.find_element(By.XPATH,"//*[@id='tenurePeriod']"))
    periodMenu.select_by_visible_text(per2)
    freqMenu = Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
    freqMenu.select_by_visible_text(frequency)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue = driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text

    #Validation
    if float(exp_mvalue) == float(act_mvalue):
        print("Test passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(1)

print("Test case passed")
driver.quit()










time.sleep(3600)

# Close the browser
driver.quit()