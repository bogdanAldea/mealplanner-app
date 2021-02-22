"""
MODULE DEFINES CONTROLLER PARENT CLASS
"""
import views


class Controller:
    """
    Class defines controller parent class and defines some general methods used across
    its child classes.
    """

    def __init__(self):
        """
        Constructor of controller parent class.
        """

        # each child that inherits the parent class will implement its own models
        # but uses the same views.
        self.models = None
        self.views = views

        # default views screen
        self.default_screen = self.views.screen.Screen()

    def validate_menu_request(self, request: int, menu_options: list) -> int:
        """
        When user is prompt to select a menu option/action, this method checks if
        the user's request is part of a list of menu options.

        :param request: int
        :param menu_options: list
        :return: int
        """

        try:
            valid_menu_request = self.models.validate_menu_request(request, menu_options)
            return valid_menu_request, True
        except self.models.exceptions.MenuOptionInvalid as e:
            self.default_screen.display_error(e)
            return None, False

    def validate_recipe_name(self, stored_recipes: list) -> str:
        """
        Method prompts user to enter a name for a new recipe and checks if the name input
        is valid by searching it in a list of stored recipes.

        :param stored_recipes: str
        :return: str
        """

        while True:
            try:
                name_request = input("\nSet recipe name >>> ")
                valid_name = self.models.validate_recipe_name(name_request, stored_recipes)
                return valid_name
            except self.models.exceptions.RecipeIsStored as e:
                self.default_screen.display_error(e)

    def validate_save_request(self, user_request: str) -> tuple:
        """
        When user is prompted with an input to save or not some data, method checks if
        user's input is a valid input.

        :param user_request: str
        :return: str
        """
        try:
            valid_save_request = self.models.validate_save_request(user_request)
            return valid_save_request, True
        except self.models.exceptions.InvalidSaveRequest as e:
            self.default_screen.display_error(e)
            return None, False