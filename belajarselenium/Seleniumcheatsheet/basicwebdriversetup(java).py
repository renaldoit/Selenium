from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By for locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Avoid time.sleep() if possible; use explicit waits

# Using WebDriverManager (Recommended)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Manual Driver Setup (Less Recommended)
# driver = webdriver.Chrome("/path/to/chromedriver")  # Specify path if needed

driver.get("https://www.example.com")
title = driver.title
print(f"Title: {title}")  # f-strings for cleaner printing

# Maximize window (optional)
driver.maximize_window()

# Get current URL
current_url = driver.current_url
print(f"Current URL: {current_url}")

driver.quit()  # Close all windows and the WebDriver session
# driver.close() # Close the current window