# Import necessary libraries 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import internal modules
from linkdin_credentials import USER_NAME, PASSWORD

# Create the Edge driver
driver = webdriver.Edge("msedgedriver.exe")

# Navigate to Linkdin
driver.get("https://www.linkedin.com/home")

# Maxime the browser window
driver.maximize_window()

# Wait a specific amount of time
time.sleep(2)

# Search for user name input and introduce the value
username_input = driver.find_element(by=By.ID, value="session_key")
username_input.send_keys(USER_NAME)

# Wait a specific amount of time
time.sleep(2)

# Search for passwors input and introduce the value
password_input = driver.find_element(by=By.ID, value="session_password")
password_input.send_keys(PASSWORD)

# Wait a specific amount of time
time.sleep(2)

# Search for login button and introduce press it
login_button = driver.find_element(by=By.CLASS_NAME, value="sign-in-form__submit-button")
login_button.send_keys(Keys.ENTER)

# Wait a specific amount of time
time.sleep(5)

# Search for Job area and click on it
driver.get("https://www.linkedin.com/jobs")

# Wait a specific amount of time
time.sleep(3)

# Search for box input (search area in jobs) 
search_input = driver.find_element(by=By.CLASS_NAME, value="jobs-search-box__text-input")
search_input.click()
search_input.send_keys("Python Developer")
search_input.send_keys(Keys.ENTER)

# Wait a specific amount of time
time.sleep(4)

# Search for region input box
region_input = driver.find_element(by=By.CLASS_NAME, value="jobs-search-box__text-input jobs-search-box__ghost-text-input")
region_input.click()
region_input.send_keys("Bucuresti")
region_input.send_keys(Keys.ENTER)

# Wait a specific amount of time
time.sleep(5)

# Exit from the program
driver.quit()
