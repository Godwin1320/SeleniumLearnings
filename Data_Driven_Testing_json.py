from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import json
 
with open(r'C:\Users\peter.godwin\OneDrive - OneWorkplace\Desktop\testdata2.json') as file:
    test_data = json.load(file)

    

for data in test_data['Sheet1']:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)

    driver.find_element(By.ID, "user-name").send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['password'])

    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    driver.quit()