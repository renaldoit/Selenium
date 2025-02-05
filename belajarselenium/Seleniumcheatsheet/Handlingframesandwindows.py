# Switching to an iframe
driver.switch_to.frame("frameId")  # Or index (less reliable)
# Interact with elements inside the iframe
driver.switch_to.default_content()  # Switch back to the main content

# Handling new windows/tabs
current_window_handle = driver.current_window_handle
for window_handle in driver.window_handles:
    if window_handle != current_window_handle:
        driver.switch_to.window(window_handle)
        break  # Switch to the new window

# Close current tab
driver.close()