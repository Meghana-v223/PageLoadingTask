from selenium import webdriver
from selenium.webdriver.common.by import By
import time
averagetime = 0
n = 10
for i in range(n):
    driver = webdriver.Chrome()
    starttime = time.time() 
    driver.get("https://mathup.com/games/crossbit?mode=championship")    
    waittime = driver.implicitly_wait(10)  
    submitButton = driver.find_element(By.XPATH, "//div[text()='Start']")
    endtime = time.time() - starttime
    averagetime = averagetime +endtime
    print(f"endtime{i}: ",endtime)
    print(f"waittime{i}: ",waittime)
    print(f"Time to load the page{i+1}: ",endtime)    
    submitButton.click()
    validate = driver.find_element(By.XPATH, "//div[text()='Easy']")  
    driver.quit()
print("Average time: ",averagetime/n)
