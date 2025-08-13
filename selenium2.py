from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
ele = driver.find_element(By.ID, "username")
ele= driver.find_element(By.NAME, "password")
ele=driver.find_element(By.XPATH, "//button[@type='submit']")

#driver.maximize_window()
print("page title", driver.title)
#time.sleep(6)
driver.close()

