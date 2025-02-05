driver.get("url")  # Simplest way to navigate
driver.back()
driver.forward()
driver.refresh()

# Other navigation methods
driver.get("another_url") # Opens a new page in the same tab
driver.execute_script("window.location = 'new_url';") # Javascript navigation