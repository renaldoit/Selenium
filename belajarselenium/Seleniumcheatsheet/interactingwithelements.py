element.click()
element.send_keys("some text")
element.clear()
element.submit()  # For form submission

# Example: Handling dropdowns
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "dropdownId"))
dropdown.select_by_value("value")  # Select by value
dropdown.select_by_index(2)  # Select by index
dropdown.select_by_visible_text("Visible Text")  # Select by visible text

# Example: Checkboxes and Radio Buttons
checkbox = driver.find_element(By.ID, "checkboxId")
if not checkbox.is_selected():
    checkbox.click()

radio_button = driver.find_element(By.ID, "radioButtonId")
radio_button.click() # No need to check if it is selected first.