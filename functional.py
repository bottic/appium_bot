import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


class Phone():
    def __init__(self, country_code: str, phone_number: str, Xscreen: int, Yscreen: int, udid: str, url: str):

        """
        Xscreen - screen size by x coordinate
        Yscreen - screen size by y coordinate
        udid - Unique device number (Example: 123.321.233.102:5555)"""

        self.country_code = country_code
        self.phone_number = phone_number
        self.Xscreen = Xscreen
        self.Yscreen = Yscreen
        self.udid = udid

        self.capabilities = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'udid': udid,
            'noReset': True,
        }
        _capabilities_option = UiAutomator2Options().load_capabilities(self.capabilities)
        self.driver = webdriver.Remote(command_executor=url, options=_capabilities_option)

    # Test click to phone
    def test_click(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Phone"]').click()

    # Automatic installation and authorization in tg account
    def install_open_tg(self, app_folder, need_install=True):
        # install tg if the need
        if need_install:
            self.driver.install_app(app_folder)

        # swipe to up and open tg
        self.driver.swipe(400, 1000, 400, 500)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Telegram').click()
        time.sleep(1)

        # click start Messaging in tg
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.TextView[@text="Start Messaging"]').click()
        time.sleep(0.5)
        # deny 1 permission
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
        self.driver.find_element(by=AppiumBy.ID,
                                 value='com.android.permissioncontroller:id/permission_deny_button').click()
        time.sleep(0.5)

        # fill phone number
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Phone number").clear().send_keys(
            self.phone_number)

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Country code').clear().send_keys(
            self.country_code)
        time.sleep(0.5)
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View').click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.TextView[@text="Yes"]').click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.TextView[@text="Continue"]').click()

        # deny 2 permission
        self.driver.find_element(by=AppiumBy.ID,
                                 value='com.android.permissioncontroller:id/permission_deny_button').click()
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button"]').click()


def check_phone_numbers_ru(phone_numbers_ru: list) -> bool:
    for i, phone in enumerate(phone_numbers_ru):
        country_code = phone[:1]
        phone_number = phone[1:]
        if len(phone_number) < 10 or len(phone_number) > 10 or len(country_code) != 1:
            print(f'In {i} line error phone_number')
            return False
    return True
