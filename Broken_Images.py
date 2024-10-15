#photos that show not found or has some error

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME, "img")
broken_images = []
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken Image found")

if broken_images:
    print(f"List of Broken Images: ")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No Broken Images")