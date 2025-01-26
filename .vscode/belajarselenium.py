from selenium import webdriver

driver = webdriver.Chrome()


driver.get("http://the-internet.herokuapp.com/login")
driver.implicitly_wait(1000)
driver.find_element(By.id, "username")
my_element.click()