from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.google.com")

element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/span/div/div[1]/div/section/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/form/div[2]/div[1]/input')
element.clear()
element.send_keys("Belajar Selenium")
time.sleep(2)

print(driver.title)
driver.quit()
#import pdb; pdb.set_trace()
#breakpoint()