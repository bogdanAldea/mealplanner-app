"""
MODULE DEFINES CREATION OF A SHOPPING LIST
"""
import models.mealplanner_model as mealplanner_model
import controllers.controller as main
import components.object_sets as obj_sets
import views


class Mealplanner(main.Controller):
    """
    Class allows user to add desired recipes to a mealplan list.
    """

    def __init__(self):
        """
        Constructor of mealplanner class.
        """
        main.Controller.__init__(self)
        self.models = mealplanner_model.MealplannerModel()

    def create_mealplan(self) -> list:
        """
        Method provides user with a list of all stored recipes ready for selection.
        :return: list
        """

        # empty list that will store recipes selected by user
        mealplan = list()

        # list of stored recipes
        recipe_data = self.models.get_recipe_data

        # render recipe selection screen
        screen = self.views.mealplanner_screen.MealplannerScreen(recipe_data)
        screen.render_screen()

        # avoid returning the list of stored recipes if empty
        try:
            assert len(recipe_data) > 0, "There are no recipes stored yet."
        except AssertionError as e:
            screen.display_error(e)

        # start selection loop
        while True:

            # get request from user to select recipes
            user_request = input("Select recipes >>> ")

            # check if user requested to exit this functionality
            if user_request in ["q", "Q"]:
                return mealplan

            elif not user_request.isdigit():
                continue

            else:
                # check if user's request is a valid recipe selector
                valid_request, option_exists = self.validate_menu_request(int(user_request), recipe_data)

                if option_exists:
                    # add selected recipe to mealplan list
                    selected_recipe = recipe_data[int(valid_request) - 1]
                    mealplan.append(selected_recipe)
                    screen.display_update(f"{selected_recipe} has been has been added to cart.")


class EarlySHoppingCart(Mealplanner):
    """
    Class breaks down all selected recipes and counts occurrences of each ingredient
    and increments its value.
    """

    def __init__(self):
        """
        Constructor of early shopping list class.
        """
        Mealplanner.__init__(self)

    def get_full_quantities(self) -> list:
        """
        Method puts together a list of ingredients sets from all recipes selected.
        :return: list
        """

        preliminary_list = dict()

        # list of selected recipes
        created_mealplan = self.create_mealplan()

        for recipe_object in created_mealplan:
            for ingredient_set in recipe_object.get_ingredients:
                preliminary_list[ingredient_set.get_name] = preliminary_list.get(ingredient_set.get_name, 0) + ingredient_set.get_quantity
        # return list of ingredient set objects
        return [obj_sets.IngredientSet(name, quantity) for name, quantity in preliminary_list.items()]


class ShoppingList(EarlySHoppingCart):
    """
    Class breaks down preliminary list of ingredients and their values and returns a new
    list of ingredient sets with new values subtracted from inventory values.
    """

    def __init__(self):
        """
        Constructor of shopping list class.
        """
        EarlySHoppingCart.__init__(self)

    def generate_shopping_list_ready(self):

        shopping_list = self.get_full_quantities()

        for inventory_item in self.models.inventory_data:
            for to_buy_set in shopping_list:
                for inventory_set in inventory_item.get_items:

                    # target the set that exists in both the shopping list & inventory
                    if to_buy_set.get_name == inventory_set.get_name:

                        # calculate the absolute subtraction of both items
                        diff = abs(to_buy_set.get_quantity - inventory_set.get_quantity)

                        if to_buy_set.get_quantity > inventory_set.get_quantity:
                            to_buy_set.set_quantity(diff)
                            inventory_new_quantity = 0

                        elif to_buy_set.get_quantity < inventory_set.get_quantity:
                            inventory_new_quantity = diff
                            shopping_list.remove(to_buy_set)

                        else:
                            inventory_new_quantity = 0
                            shopping_list.remove(to_buy_set)

                        inventory_set.set_quantity(inventory_new_quantity)

        self.models.save_inventory_data()
        return shopping_list

    def sort_by_type(self, shopping_list: list) -> dict:
        """
        Method takes the list of needed ingredients for selected recipes and sorts each ingredient set
        by its specific type (meat, vegetable, dairy etc.).
        :param shopping_list: list
        :return: dict
        """

        # generate dictionary with component types as keys and empty lists as default values
        sorted_shopping_list = {component_type: list() for component_type in self.models.installed_components.keys()}

        # component data for ingredient comparison and sorting to specific type list
        component_data = self.models.component_data

        for component in component_data:
            for recipe_set in shopping_list:

                if recipe_set.get_name in component.get_obj_items:
                    type_target = sorted_shopping_list.get(component.get_obj_type)
                    type_target.append(recipe_set)

        return sorted_shopping_list