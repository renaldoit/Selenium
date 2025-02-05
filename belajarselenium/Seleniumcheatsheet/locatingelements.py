element = driver.find_element(By.ID, "elementId")
element = driver.find_element(By.NAME, "elementName")
element = driver.find_element(By.CLASS_NAME, "elementClassName")
element = driver.find_element(By.TAG_NAME, "tagName")
element = driver.find_element(By.LINK_TEXT, "link text")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
element = driver.find_element(By.CSS_SELECTOR, "cssSelector")  # Preferred for flexibility
element = driver.find_element(By.XPATH, "xpathExpression")  # Use with caution, can be brittle

elements = driver.find_elements(By.CSS_SELECTOR, "someCssSelector")  # Find multiple elements

# Example: Accessing element properties
attribute_value = element.get_attribute("attributeName")
element_text = element.text
is_displayed = element.is_displayed()
is_enabled = element.is_enabled()
is_selected = element.is_selected()