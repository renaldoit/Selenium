driver.save_screenshot("screenshot.png")  # Saves to the current directory

# For more control over file paths:
import os
screenshot_path = os.path.join("screenshots", "my_screenshot.png")  # Create a "screenshots" folder
driver.save_screenshot(screenshot_path)