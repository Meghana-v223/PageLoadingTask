from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

averagetime = 0
n = 10

for i in range(n):
    driver = webdriver.Chrome()    
    starttime = time.time()  # Start timing before page load
    driver.get("https://mathup.com/games/crossbit?mode=championship")
    
    try:
        submitButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Start']"))
        )
    except:
        print(f"Failed to load page {i+1}")
        driver.quit()
        continue

    endtime = time.time() - starttime  # Time taken to reach this point
    averagetime += endtime

    print(f"Iteration {i+1}: Page Load Time = {endtime:.2f} seconds")
    
    submitButton.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Easy']"))
        )
    except:
        print(f"Validation step failed in iteration {i+1}")

    driver.quit()

print(f"Average page load time: {averagetime/n:.2f} seconds")
