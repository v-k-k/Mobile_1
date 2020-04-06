from pages.pages import *
import os


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.additional_info_page = AdditionalInfoPage(driver)
        self.favorite_page = FavoritePage(driver)

    @staticmethod
    def app_dir():
        curr_dir = os.getcwd()
        splitter = os.sep
        if os.name == 'nt':
            splitter = os.sep * 2
        tmp = curr_dir.split(splitter) + ["app_bin", "Boxing Timer.apk"]
        return splitter.join(tmp)
