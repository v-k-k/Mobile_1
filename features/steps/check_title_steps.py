from behave import given, when, then


@given('Tap on "Settings" button, make sound louder and check if it was really done')
def tap_settings(context):
    context.app.main_page.click_settings()


@when('click {clicks} times on break seconds tap on "Add to favorites"')
def add_to_favorites(context, clicks):
    context.app.settings_page.increase_break_time(clicks)
    context.app.settings_page.get_training_time()
    context.app.settings_page.get_break_time()
    context.app.settings_page.check_sound_level()


@then('New window contains the {placeholder} placeholder')
def check_placeholder(context, placeholder):
    context.app.settings_page.check_placeholder(placeholder)


@then('App info contains {app_pattern} in window title')
def check_app_info(context, app_pattern):
    context.app.settings_page.window_ok()
    context.app.settings_page.open_about_page()
    context.app.settings_page.evaluate()
    context.app.settings_page.get_info_title(app_pattern)


@then('System info contains {app_pattern} in app title')
def check_sys_app_info(context, app_pattern):
    context.app.additional_info_page.get_info_title(app_pattern)


@then('Saved settings contains {title} in title')
def check_favorites_title(context, title):
    context.app.settings_page.send_title(title)
    context.app.settings_page.window_ok()
    context.app.settings_page.back_to_main()
    context.app.main_page.click_favorite()
    context.app.favorite_page.check_saved_title(title)


@then('training time is {training_time}')
def check_saved_training_time(context, training_time):
    context.app.favorite_page.check_saved_training_time(training_time)


@then('break time is {break_time} after 3 clicks')
def check_saved_break_time(context, break_time):
    context.app.favorite_page.check_saved_break_time(break_time)

