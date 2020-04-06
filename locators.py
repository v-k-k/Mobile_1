from selenium.webdriver.common.by import By


class MainPageLocators:
    SETTINGS_BUTTON = (By.ID, "com.nulltree.roundbell:id/setting_button")
    FAVORITE_BUTTON = (By.ID, "com.nulltree.roundbell:id/favorite_button")


class SettingsPageLocators:
    INCREASE_MINUTES_BREAK = (By.ID, "com.nulltree.roundbell:id/break_up")
    TRAINING_TIME = (By.ID, "com.nulltree.roundbell:id/training_time")
    BREAK_TIME = (By.ID, "com.nulltree.roundbell:id/break_time")
    SEEK_BAR = (By.ID, "com.nulltree.roundbell:id/sb_volume")
    BELL_BUTTON = (By.ID, "com.nulltree.roundbell:id/btn_listen")
    OPEN_FAVORITES_WINDOW = (By.XPATH, "//*[@resource-id='com.nulltree.roundbell:id/ll_favorite']"
                                       "/android.widget.LinearLayout/android.widget.ImageView")
    ABOUT_APP = (By.XPATH, "//*[@resource-id='com.nulltree.roundbell:id/ll_app_info']"
                           "/android.widget.LinearLayout/android.widget.ImageView")


class FavoriteTitleLocators:
    PLACEHOLDER = (By.ID, "com.nulltree.roundbell:id/et_title")
    CLICK_OK = (By.ID, "android:id/button1")


class AboutAppLocators:
    EVALUATE = (By.ID, "com.nulltree.roundbell:id/tv_evaluate")


class AlertWindowLocators:
    TITLE = (By.ID, "android:id/alertTitle")
    APP_INFO = (By.ID, "android:id/aerr_app_info")


class AppInfoLocators:
    TITLE = (By.ID, "com.android.settings:id/entity_header_title")


class FavoritePageLocators:
    TITLE = (By.ID, "com.nulltree.roundbell:id/tv_title")
    TRAINING_TIME = (By.ID, "com.nulltree.roundbell:id/tv_training_time")
    BREAK_TIME = (By.ID, "com.nulltree.roundbell:id/tv_break_time")
