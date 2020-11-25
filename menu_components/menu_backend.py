from mealplanner_app.menu_components.menu_views import *


def menu_template(available_menu_options, menu_text_display):
    user_request = MenuValues.DEFAULT
    while user_request not in available_menu_options:
        while True:
            try:
                user_request = int(input(menu_text_display))
                return user_request
            except ValueError:
                print("Eroare input: optiune invalida. Optiunile valide sunt: ", available_menu_options)


def get_main_menu():
    menu = menu_template(available_menu_options=MenuValues.MAIN_MENU_OPTIONS,
                         menu_text_display=MenuTexts.MAIN_MENU)
    return menu


def get_mealplanner_menu():
    menu = menu_template(available_menu_options=MenuValues.MEALPLANNER_OPTIONS,
                         menu_text_display=MenuTexts.MEALPLANNER_MENU)
    return menu


def get_edit_menu():
    menu = menu_template(available_menu_options=MenuValues.EDIT_OPTIONS,
                         menu_text_display=MenuTexts.EDIT_MENU)
    return menu