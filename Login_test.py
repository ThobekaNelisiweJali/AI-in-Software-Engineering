from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Set a wait timeout
wait = WebDriverWait(driver, 10)

# ---------- VALID LOGIN TEST ----------
print("\n🔐 VALID LOGIN TEST")
valid_username = input("Enter VALID username (e.g. student): ")
valid_password = input("Enter VALID password (e.g. Password123): ")

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for fields to load and enter details
wait.until(EC.presence_of_element_located((By.ID, "username")))
driver.find_element(By.ID, "username").send_keys(valid_username)
driver.find_element(By.ID, "password").send_keys(valid_password)
driver.find_element(By.ID, "submit").click()

# Wait and check for success message
time.sleep(2)
if "Logged In Successfully" in driver.page_source:
    print("✅ Valid login test PASSED")
else:
    print("❌ Valid login test FAILED")

# ---------- INVALID LOGIN TEST ----------
print("\n🔐 INVALID LOGIN TEST")
invalid_username = input("Enter INVALID username (e.g. wrongUser): ")
invalid_password = input("Enter INVALID password (e.g. wrongPass): ")

# Reload the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

wait.until(EC.presence_of_element_located((By.ID, "username")))
driver.find_element(By.ID, "username").send_keys(invalid_username)
driver.find_element(By.ID, "password").send_keys(invalid_password)
driver.find_element(By.ID, "submit").click()

# Wait and check for error message
time.sleep(2)
if "Your username is invalid!" in driver.page_source:
    print("✅ Invalid login test PASSED")
else:
    print("❌ Invalid login test FAILED")

# Keep the browser open for review
input("\nPress Enter to close the browser...")
driver.quit()
