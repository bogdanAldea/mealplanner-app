"""
MODULE HANDLES THE SELECTION OF AN INGREDIENT
"""
import settings
import controllers.controller as main
import models.components_model as component_model


class IngredientSelector(main.Controller):
    """
    Child class of Controller parent class that defines functionality of selecting
    a desired ingredient from the menu and returning it.
    """

    def __init__(self):
        """
        Constructor of ingredient selector class.
        """

        main.Controller.__init__(self)

        # model for component selection
        self.models = component_model.ComponentModel(settings.INGREDIENTS_JSON_PATH)

    def get_ingredient(self, ingredients_list: list, recipe_status: dict) -> str:
        """
        Main method that handles selection of ingredients.

        :param ingredients_list: list
        :param recipe_status: dict
        :return: str
        """

        # SCREEN RENDERING HERE
        screen = self.views.selectors_screens.IngredientSelectorScreen(ingredients_list, recipe_status)
        screen.render_screen()

        while True:
            # get user request for selection of an ingredient
            user_request = input("\nSelect ingredient >>> ")

            # check if request from user is or is not a values for exit / back
            if user_request in ["q", "Q"]:
                return None,  user_request

            else:
                # check if user's request exists as part of the ingredient list
                valid_request, option_exists = self.validate_menu_request(int(user_request), ingredients_list)

                if option_exists:
                    selected_ingredient = self.models.select_from_values(int(valid_request), ingredients_list)
                    return selected_ingredient, valid_request

                else:
                    continue