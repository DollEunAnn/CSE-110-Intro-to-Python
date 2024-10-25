import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load Excel file
excel_file = 'form_details.xlsx'
data = pd.read_excel(excel_file)

# Path to WebDriver
driver_path = '/path/to/chromedriver'  # Change to the path where you downloaded the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# URL of the form
form_url = 'https://example.com/form'
driver.get(form_url)

# Iterate through each row in the Excel file
for index, row in data.iterrows():
    # Fill the form fields using the row data
    driver.find_element(By.NAME, 'first_name').send_keys(row['First Name'])
    driver.find_element(By.NAME, 'last_name').send_keys(row['Last Name'])
    driver.find_element(By.NAME, 'email').send_keys(row['Email'])
    driver.find_element(By.NAME, 'phone').send_keys(row['Phone'])

    # Submit the form
    driver.find_element(By.NAME, 'submit').click()

    # Wait for a bit to allow the form to submit and move to the next iteration
    time.sleep(3)

    # Return to the form page if needed
    driver.get(form_url)

# Close the browser when done
driver.quit()
