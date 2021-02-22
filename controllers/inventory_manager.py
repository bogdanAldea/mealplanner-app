"""
MODULE HANDLES THE MANAGEMENT OF THE INVENTORY DATA
"""
import models.inventory_model as inventory
import controllers.controller as controller
import settings


class InventoryManager(controller.Controller):
    """
    Class inherits the Controller parent class that handles all inventory
    data manipulation.
    """

    def __init__(self):
        """
        Constructor of inventory manager class.
        """
        controller.Controller.__init__(self)
        self.models = inventory.InventoryModel(settings.INVENTORY_JSON_PATH)

    @property
    def get_inventory_data(self):
        return self.models.inventory_data

    def get_component_values(self) -> list:
        """
        Method handles the first step in updating desired inventory items by selecting components
        and returning their list of values.
        :return:
        """

        # generated list of all inventory components types to use as menu
        inventory_comp_menu = [components.get_type for components in self.get_inventory_data]

        # rendering inventory screen
        screen = self.views.inventory_screens.InventoryScreen(inventory_comp_menu)
        screen.render_screen()

        while True:
            # get user request for a component selection
            user_request = input("\nSelect component >>> ")

            # check if user's request is or is not a values for exit / back
            if user_request in ["q", "Q"]:
                return None, user_request

            else:
                # check is user's request ia a valid menu option
                valid_request, option_exists = self.validate_menu_request(int(user_request), inventory_comp_menu)

                if option_exists:

                    # return list of values based on the selected component's type
                    component_type = inventory_comp_menu[int(user_request)-1]
                    component_values = self.models.get_item(component_type)

                    # avoid returning an empty list
                    try:
                        assert len(component_values.get_items) > 0, f"<{component_type}> has no values stored."
                        return component_values.get_items, valid_request
                    except AssertionError as e:
                        screen.display_error(e)
                        continue

                else:
                    continue

    def get_ingredient(self, selected_component_values: list) -> object:
        """
        Method handles the second step of updating one of the ingredient's quantity.
        :param selected_component_values: list
        :return: object
        """

        # generated list of ingredients used to display as menu
        ingredients_menu = [ingredient.get_name for ingredient in selected_component_values]

        # screen rendering
        screen = self.views.inventory_screens.InventoryScreen(ingredients_menu)
        screen.render_screen()

        while True:
            # get user's request for ingredient selection
            user_request = input("\nSelect ingredient >>> ")

            # check if user's input is or is not a values for exit / back
            if user_request in ["q", "Q"]:
                return None, user_request

            else:
                # check if user's request is a valid menu option
                valid_request, option_exists = self.validate_menu_request(int(user_request), ingredients_menu)

                if option_exists:
                    # return selected ingredient's values
                    selected_ingredient = selected_component_values[int(valid_request)-1]
                    return selected_ingredient, user_request

                else:
                    continue

    def update_quantities(self) -> None:
        """
        Method updated the current quantity of the selected ingredient.
        :return: None
        """

        while True:
            # ask user to select an component and return the list of ingredients
            selected_component, user_request = self.get_component_values()

            # check if user's input is or is not a value for exit / back
            if user_request in ["q", "Q"]:
                break

            else:
                # ask user to select an ingredient from the returned list of ingredients
                selected_ingredient, user_request = self.get_ingredient(selected_component)

                # check if user's request is or is not a value for back / exit
                if user_request in ["q", "Q"]:
                    break

                else:
                    # set new quantity for ingredient
                    new_quantity = int(input(f"New quantity for {selected_ingredient.get_name} >>> "))
                    selected_ingredient.set_quantity(new_quantity)

    def sort_ingredient(self, new_ingredient) -> None:
        """
        Method takes a new ingredient as a param and sorts it.
        :param new_ingredient: object
        :return: None
        """
        self.models.sort_ingredient(new_ingredient)

    def save_inventory_data(self) -> None:
        self.models.save_inventory_data()