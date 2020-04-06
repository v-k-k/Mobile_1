from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import *


class MainPage(BasePage):

    def click_settings(self):
        settings = self.wait.until(EC.presence_of_element_located(MainPageLocators.SETTINGS_BUTTON))
        settings.click()

    def click_favorite(self):
        favorite = self.wait.until(EC.presence_of_element_located(MainPageLocators.FAVORITE_BUTTON))
        favorite.click()


class SettingsPage(BasePage):

    def increase_break_time(self, n):
        minutes_break = self.wait.until(EC.presence_of_element_located(SettingsPageLocators.INCREASE_MINUTES_BREAK))
        for _ in range(int(n)):
            minutes_break.click()

    def get_training_time(self):
        training_time = self.wait.until(EC.presence_of_element_located(SettingsPageLocators.TRAINING_TIME))
        return training_time.text

    def get_break_time(self):
        break_time = self.wait.until(EC.presence_of_element_located(SettingsPageLocators.BREAK_TIME))
        return break_time.text

    def check_sound_level(self):
        self.mover(self.action, 10, 550, 10, 50)
        get_seekbar = self.wait.until(EC.presence_of_element_located(SettingsPageLocators.SEEK_BAR))
        start = get_seekbar.location.get('x')
        end = get_seekbar.size.get('width')
        ycd = get_seekbar.location.get('y')
        self.mover(self.action, start, ycd, end, ycd)
        self.wait.until(EC.presence_of_element_located(SettingsPageLocators.BELL_BUTTON)).click()
        self.mover(self.action, 10, 850, 10, 30)
        self.wait.until(EC.presence_of_element_located(SettingsPageLocators.OPEN_FAVORITES_WINDOW)).click()
        self.window = self.wait.until(EC.presence_of_element_located(FavoriteTitleLocators.PLACEHOLDER))

    def check_placeholder(self, placeholder):
        assert self.window.text == placeholder

    def send_title(self, check_title):
        self.window.send_keys(check_title)

    def window_ok(self):
        self.wait.until(EC.presence_of_element_located(FavoriteTitleLocators.CLICK_OK)).click()

    def open_about_page(self):
        #driver.press_keycode(66)
        self.wait.until(EC.presence_of_element_located(SettingsPageLocators.ABOUT_APP)).click()

    def evaluate(self):
        self.wait.until(EC.presence_of_element_located(AboutAppLocators.EVALUATE)).click()

    def get_info_title(self, app_pattern):
        try:
            title = self.wait.until(EC.presence_of_element_located(AlertWindowLocators.TITLE))
        except TimeoutException:
            self.mover(self.action, 10, 550, 10, 50)
            self.mover(self.action, 10, 850, 10, 50)
            self.open_about_page()
            self.evaluate()
            title = self.wait.until(EC.presence_of_element_located(AlertWindowLocators.TITLE))
        assert app_pattern in title.text


class AdditionalInfoPage(BasePage):

    def get_info_title(self, app_pattern):
        self.wait.until(EC.presence_of_element_located(AlertWindowLocators.APP_INFO)).click()
        app_name = self.wait.until(EC.presence_of_element_located(AppInfoLocators.TITLE))
        assert app_pattern in app_name.text


class FavoritePage(BasePage):

    def check_saved_title(self, title):
        saved_title = self.wait.until(EC.presence_of_element_located(FavoritePageLocators.TITLE))
        assert title == saved_title.text

    def check_saved_training_time(self, training_time):
        saved_training_time = self.wait.until(EC.presence_of_element_located(FavoritePageLocators.TRAINING_TIME))
        assert saved_training_time.text == training_time

    def check_saved_break_time(self, break_time):
        saved_break_time = self.wait.until(EC.presence_of_element_located(FavoritePageLocators.BREAK_TIME))
        assert break_time == saved_break_time.text

