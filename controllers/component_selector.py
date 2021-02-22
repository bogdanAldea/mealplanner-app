"""
MODULE DEFINES CLASSES FOR SELECTING INGREDIENTS & COMPONENTS
"""
import settings
import controllers.controller
import models.components_model as component_models


class ComponentSelector(controllers.controller.Controller):
    """
    Child class of Controller parent class that handles the selection
    functionality of a component type.

    Class inherits Controller parent class in order to use its general methods.
    This class connects the views and models that allows user to request a component type
    via its views and returns selected component's values.
    """

    def __init__(self):
        """
        Constructor of component selector class
        """
        controllers.controller.Controller.__init__(self)

        # model for component selector business logic.
        self.models = component_models.ComponentModel(settings.INGREDIENTS_JSON_PATH)

    def get_component(self, components_list, recipe_status, sorting) -> list:
        """
        Method uses a list of all components type to display a menu.
        Asks user for an input which selects one of the components
        and returns its values back to the user. The "sorting" attr, if false, makes
        sure that the returned list of values is not empty.

        :param components_list: list
        :param recipe_status: dict
        :param sorting: bool
        :return: list
        """

        # views screen rendering
        screen = self.views.selectors_screens.ComponentSelectorScreen(components_list, recipe_status)
        screen.render_screen()

        while True:
            # get user request for a component selection
            user_request: str = input("\nSelect component >>> ")

            # check if user's request is or is not a values for exit or back
            if user_request in ["q", "Q"]:
                return None, user_request

            else:
                # if user didn't ask to exit this method, check if the input for ne of the components
                # is a valid one.
                valid_request, option_exists = self.validate_menu_request(int(user_request), components_list)

                if option_exists:
                    component_type = components_list[int(valid_request)-1]
                    # filter component types and return the list of values and "sorting" attr value
                    ingredient_values, sorting_enabled = self.filter_component_values(component_type, sorting)

                    # method returns the list of values only if the sorting action is True:
                    if sorting_enabled:
                        return ingredient_values, valid_request

                    # if method doesn't require sorting of new ingredients and
                    # the list of values returned is empty, prompts user for another request
                    else:
                        continue

                else:
                    # if user's request for a menu option is invalid, an exception is raised and
                    # method prompts user for another request
                    continue

    def filter_component_values(self, selected_component_type: str, sorting_action) -> list:
        """
        Method takes user's request for a component type and returns its values back to him
        :param selected_component_type: str
        :param sorting_action: bool
        :return: list
        """

        try:
            # method tries to filter components and return the request list of values
            # if context needs for ingredients to be sort by their type and added to
            # selected values, sorting_action attr returns True if list of values is empty.
            selected_values = self.models.filter_values(selected_component_type, sorting_action)
            return selected_values, True

        except self.models.exceptions.EmptyListOfValues as e:
            # if context doesn't require sorting and the returned list of values is empty
            # method returns False
            self.default_screen.display_error(e)
            return None, False

    def sort(self, new_ingredient: object, target_values: list) -> bool:
        """
        When used, method takes an ingredient object and a selected list of values,
        and adds the ingredient to that list.
        :param new_ingredient: object
        :param target_values: list
        :return: bool
        """

        try:
            # if ingredient was not found in the list, it will be appended
            self.models.sort_ingredient(new_ingredient, target_values)
            return True

        except self.models.exceptions.IngredientIsStored as e:
            # if ingredient was found, exception is raised
            self.default_screen.display_error(e)
            return False

    def save_component_data(self):
        self.models.save_component_data()