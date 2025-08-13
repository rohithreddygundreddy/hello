from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# -------------------------
# CONFIGURATION
# -------------------------
LOGIN_URL = "file:///C:/Users/Boys/hello/file1.html"  # Replace with your login page URL
EMAIL = "test@example.com"               # Test email
PASSWORD = "pass1234"                # Test password

# -------------------------
# START SELENIUM
# -------------------------
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
driver.maximize_window()

# Open the login page
driver.get(LOGIN_URL)
time.sleep(2)  # wait for the page to load

# -------------------------
# ENTER LOGIN DETAILS
# -------------------------
email_field = driver.find_element(By.NAME, "email")   # or By.ID / By.XPATH depending on page
password_field = driver.find_element(By.NAME, "password")

email_field.clear()
password_field.clear()

email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.RETURN)  # Press Enter to submit

time.sleep(3)  # wait for login to process

# -------------------------
# VERIFY LOGIN SUCCESS
# -------------------------
try:
    # Example: check if a logout button exists after login
    driver.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
    print("✅ Login successful!")
except:
    print("❌ Login failed!")

# Close browser
driver.quit()
