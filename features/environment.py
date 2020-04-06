from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):

    caps = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "Android Emulator",
        "app": Application.app_dir()
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()

