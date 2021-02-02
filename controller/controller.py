"""
"""
import models
import views
import os


class Controller:
    EXCEPTIONS = models.exceptions

    def __init__(self, VIEWS, MODELS):
        self.models: models.models = MODELS
        self.views: views = VIEWS

    def component_selector(self, components_list, recipe_status):

        # print menu to the screen via views class
        component_screen = self.views.ComponentSelector(components_list, recipe_status)
        component_screen.render_screen()

        # get user request for component selection
        while True:
            component_selection_request = input("\nSelect component >>> ")

            # check if request is value of exit/back
            if component_selection_request in ["q", "Q"]:
                return None, component_selection_request

            else:

                # check if request is a valid choice from range of len(components_list)
                if int(component_selection_request) not in range(1, len(components_list)+1):
                    continue

                else:
                    ingredient_values = self.models.component_creator.select_component_values(request=int(component_selection_request))
                    return ingredient_values, component_selection_request

    def ingredient_selector(self, ingredients_list, recipe_status):

        # print menu to the screen via views class
        ingredient_screen = self.views.IngredientSelector(ingredient_menu_list=ingredients_list, recipe_status=recipe_status)
        ingredient_screen.render_screen()

        # get user request for ingredient selection
        while True:
            ingredient_selection_request = input("\nSelect ingredient >>> ")

            # check if request is value of exit/back
            if ingredient_selection_request in ["q", "Q"]:
                return None, None, ingredient_selection_request

            else:

                # check if request is a valid choice from range of len(ingredients_list)
                if int(ingredient_selection_request) not in range(1, len(ingredients_list)+1):
                    continue

                else:
                    selected_ingredient = self.models.component_creator.select_from_values(request=int(ingredient_selection_request),
                                                                                           values=ingredients_list)
                    selected_quantity = int(input("Quantity >>> "))
                    return selected_ingredient, selected_quantity, ingredient_selection_request

    def validate_recipe_name(self):

        # list of all recipe names already stored
        inventory = [recipe.get_name for recipe in self.models.recipe_creator.recipe_objects]

        # filter requested name and return if not found in inventory
        while True:
            try:
                recipe_name = input("Set name >>> ")
                valid_name = self.models.validate_recipe_name(name_request=recipe_name, recipe_inventory=inventory)
                return valid_name
            except Controller.EXCEPTIONS.RecipeIsStored as e:
                print(e.args[0])

    def create_recipe(self):

        # refresh and clear screen
        screen = self.views.Create_Recipe()
        screen.render_screen()

        # recipe blueprint class instance
        recipe_blueprint = self.models.recipe_creator.get_recipe_blueprint()

        # recipe name var
        recipe_name = self.validate_recipe_name()

        # recipe ingredients var
        recipe_ingredients = dict()

        # recipe status (informative purpose)
        recipe_status = {
            "Recipe name": recipe_name,
            "Recipe ingredients": recipe_ingredients}

        # components list for views to display as menu
        components = self.models.component_creator.installed_components.keys()

        # start loop
        while True:

            # unpack returned values from component_selector method
            selected_component, menu_request = self.component_selector(components_list=components, recipe_status=recipe_status)

            # check if requested option is not a value for exit/back
            if menu_request not in ["q", "Q"]:

                # unpack values from ingredient_selector method
                ingredient, quantity, menu_request = self.ingredient_selector(ingredients_list=selected_component, recipe_status=recipe_status)

                # check if ingredient request is not a value of exit/back
                if menu_request not in ["q", "Q"]:
                    recipe_ingredients[ingredient] = quantity

            else:
                break

        # create recipe object with selected items
        recipe_object = recipe_blueprint(name=recipe_name, ingredients=recipe_ingredients)
        return recipe_object

    def save_recipe(self, recipe_to_save):

        # refresh and clear screen / render save screen
        save_screen = self.views.SaveRecipe(recipe_to_save)
        save_screen.render_screen()

        # prompt user to save /not save recipe
        while True:
            try:
                request = self.validate_save_request()

                if request in ["y", "Y"]:

                    recipe = recipe_to_save.__dict__
                    self.models.save_recipe(recipe)
                    save_screen.display_saving_status(status="Recipe is being saved...")
                    break

                elif request in ["n", "N"]:
                    print("recipe not saved...")
                    break
            except Controller.EXCEPTIONS.InvalidSaveRequest as e:
                save_screen.display_error(exception_error=e)
                continue

    @staticmethod
    def validate_save_request():
        save_request = input("\nWant to save recipe? >>> ")
        if save_request in ["y", "Y"] or save_request in ['n', "N"]:
            return save_request
        else:
            raise Controller.EXCEPTIONS.InvalidSaveRequest("Option invalid. The valid options are Y/y or Q/q.")