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
        tmp = curr_dir.split('\\') + ["app_bin", "Boxing Timer.apk"]
        double_splitter = '\\' * 2
        return double_splitter.join(tmp)