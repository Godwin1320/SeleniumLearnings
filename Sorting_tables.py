from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()

Sorted = []
# Click on the last name column to sort it
driver.find_element(By.XPATH, "//span[@class='first-name']").click()

# Find all last names in the table
names = driver.find_elements(By.XPATH, "//table[@id='table2']//tr/td[2]")


for ele in names:
    Sorted.append(ele.text)  # Append the text of each element to the Sorted list

original = Sorted.copy()  # Copy the original list
Sorted.sort()  # Sort the copied list
print(Sorted)
print(original)
# Assert that the list is sorted
assert original == Sorted, "The list is not sorted correctly."

driver.quit()
