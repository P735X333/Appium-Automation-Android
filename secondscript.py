from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Your_Device_Name',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'UiAutomator2'
}

# Connect to the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the settings app to load
driver.implicitly_wait(10)

# Navigate to the Battery section
try:
    # Find the battery element by resource ID
    battery_element = driver.find_element(MobileBy.ID, 'android:id/title')
    battery_element.click()
except NoSuchElementException:
    print("Battery section not found")

# Close the Appium session
driver.quit()
