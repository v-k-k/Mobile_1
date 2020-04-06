from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = TouchAction(driver)
        self.wait = WebDriverWait(driver, 10)
        self.window = None

    @staticmethod
    def mover(act, x1, y1, x2, y2):
        return act.press(None, x1, y1, None).wait().move_to(None, x2, y2).release().perform()

    def back_to_main(self):
        for _ in range(2):
            self.driver.back()
