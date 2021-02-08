"""
"""
import models


class Controller:

    exceptions = models.exceptions

    def __init__(self, VIEWS, MODELS):
        self.models = MODELS
        self.views = VIEWS

    """
    HELPER METHODS FOR HANDLING ERRORS    
    """

    def validate_recipe_name(self):

        # init screen manager
        screen = self.views.screen_manager.ScreenManager()

        # list of all recipes names already stored
        inventory = [recipe.get_name for recipe in self.models.recipe_creator.recipe_objects]

        # filter requested name and return if not found in inventory
        while True:
            try:
                requested_recipe_name = input("Set name >>> ")
                valid_name = self.models.validate_recipe_name(name_request=requested_recipe_name, recipe_inventory=inventory)
                return valid_name
            except Controller.exceptions.RecipeIsStored as e:
                screen.display_error_message(e)

    def validate_save_request(self):

        # init screen manager
        screen = self.views.screen_manager.ScreenManager()

        options = ["y", "Y", "n", "N"]
        while True:
            try:
                save_request = input("\nWant to save your data? >>> ")
                valid_request = self.models.validate_save_request(request=save_request, options=options)
                return valid_request
            except Controller.exceptions.InvalidSaveRequest as e:
                screen.display_error_message(e)

    def validate_menu_request(self, request, menu_options):

        # init screen manager
        screen = self.views.screen_manager.ScreenManager()

        while True:
            try:
                valid_menu_request = self.models.validate_menu_request(request, menu_options)
                return valid_menu_request, True
            except Controller.exceptions.MenuOptionInvalid as e:
                screen.display_error_message(e)
                return None, False

    def validate_ingredient_name(self, component_values):

        # init screen manager
        screen = self.views.screen_manager.ScreenManager()

        try:
            requested_ingredient_name = input("Set ingredient name >>> ")
            valid_request = self.models.validate_ingredient_name(name_request=requested_ingredient_name, stored_values=component_values)
            return valid_request, True
        except Controller.exceptions.IngredientIsStored as e:
            screen.display_error_message(e)
            return None, False