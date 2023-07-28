import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




def case1():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Your_Device_Name',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'UiAutomator2'
    }

    # Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("App Installation Initiated")
    # Path to the APK file
    apk_path = "C:/Users/tejas/PycharmProjects/AppiumProject/apkfiles/"
    updated_apk_path = apk_path + application + ".apk"

    # Install the APK
    driver.install_app(updated_apk_path)
    print("App Installation completed successfully")
    time.sleep(15)
    driver.quit()

def case2():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Your_Device_Name',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'UiAutomator2'
    }

    # Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("Activation of device admin permission initiated")

    # Navigate to the "Settings" section
    try:
        # Find the "Settings" option by resource ID and click on it

        # element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Battery")')
        element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().resourceId("com.android.settings:id/search_action_bar")')
        # element.send_keys("device admin")
        action = TouchAction(driver)
        action.tap(element).perform()
        time.sleep(10)
        driver.press_keycode(32)  # "D"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(50)  # "V"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(31)  # "C"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(62)  # " "
        driver.press_keycode(29)  # "A"
        driver.press_keycode(32)  # "D"
        driver.press_keycode(41)  # "M"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(42)  # "N"

        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Security & location")').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device admin apps")').click()
        time.sleep(5)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, i_automator_string).click()
        time.sleep(5)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Activate this device admin app")').click()
        driver.press_keycode(3)
        print("Device admin permission activated successfully for the installed app")
        driver.quit()
    except NoSuchElementException:
        print("Settings section not found and could not activate device admin permission")

def case3():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Your_Device_Name',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'UiAutomator2'
    }

    # Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("Deactivation of device admin permission initiated")


    # Navigate to the "Settings" section
    try:
        # Find the "Settings" option by resource ID and click on it

        # element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Battery")')
        element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().resourceId("com.android.settings:id/search_action_bar")')
        # element.send_keys("device admin")
        action = TouchAction(driver)
        action.tap(element).perform()
        time.sleep(10)
        driver.press_keycode(32)  # "D"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(50)  # "V"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(31)  # "C"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(62)  # " "
        driver.press_keycode(29)  # "A"
        driver.press_keycode(32)  # "D"
        driver.press_keycode(41)  # "M"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(42)  # "N"

        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Security & location")').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device admin apps")').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, i_automator_string).click()
        time.sleep(5)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Deactivate this device admin app")').click()
        time.sleep(5)
        if application == "AppLock":
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
            print("clicked applock ok button")
        else:
            print("not clicked")
        driver.press_keycode(3)
        print("Device admin permission is successfully Deactivated")
        driver.quit()
    except NoSuchElementException:
        print("Settings section not found/Could not deactivate device admin permission")


def case4():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Your_Device_Name',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'automationName': 'UiAutomator2'
    }

    # Connect to the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("Uninstallation of the app initiated")

    # Navigate to the "Settings" section
    try:
        # Find the "Settings" option by resource ID and click on it

        # element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Battery")')
        element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                      'new UiSelector().resourceId("com.android.settings:id/search_action_bar")')
        # element.send_keys("device admin")
        action = TouchAction(driver)
        action.tap(element).perform()
        time.sleep(10)
        driver.press_keycode(32)  # "D"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(50)  # "V"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(31)  # "C"
        driver.press_keycode(33)  # "E"
        driver.press_keycode(62)  # " "
        driver.press_keycode(29)  # "A"
        driver.press_keycode(32)  # "D"
        driver.press_keycode(41)  # "M"
        driver.press_keycode(37)  # "I"
        driver.press_keycode(42)  # "N"

        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Security & location")').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Device admin apps")').click()
        time.sleep(3)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, i_automator_string).click()
        time.sleep(3)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Uninstall app")').click()
        time.sleep(3)
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
        time.sleep(5)
        print("App uninstallation is successful")
        driver.quit()

    except NoSuchElementException:
        print("Settings section not found and could not uninstall app")


def switch_case(case):
    switch = {
        1: case1,
        2: case2,
        3: case3,
        4: case4
    }
    return switch.get(case)()

#'Nova Launcher'


applicationsList = ['Kaspersky', 'AnyDesk', 'AppLock']

for application in applicationsList:
    print(application)
    i_automator_string = 'new UiSelector().text("{}")'.format(application)
    switch_case(1)  # Output: "Install app"
    switch_case(2)  # Output: "Activate device admin permission"
    switch_case(3)  # Output: "Deactivate device admin permission if enabled"
    switch_case(4)  # Output: "Unintall app"

# Close the Appium session

