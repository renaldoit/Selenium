from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://www.facebook.com")

element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("testemail@gmail.com")

element_pass = driver.find_element(By.ID, "pass")
element_pass.clear()
element_pass.send_keys("testpassword")

login_button_element = driver.find_element(By.NAME, "login")
login_button_element.click()

time.sleep(5)

print(driver.title)

driver.quit()