"""
"""
import recipe
import components
import settings
import models.exceptions as exceptions


class Model:

    def __init__(self):
        self.recipe_file = settings.RECIPES_JSON_PATH
        self.components_file = settings.COMPONENTS_JSON_PATH
        self.installed_components = settings.INSTALLED

        self.recipe_creator = recipe.recipe_creator.RecipeCreator(database_path=self.recipe_file)
        self.component_creator = components.component_creator.ComponentCreator(database_path=self.components_file,
                                                                               installed_components=self.installed_components)

    def save_recipe(self, new_recipe):

        recipe_dict = new_recipe.__dict__
        self.recipe_creator.save(data_to_save=recipe_dict)

    def save_component(self, new_component: dict):
        ...

    def validate_recipe_name(self, name_request, recipe_inventory):
        if self.recipe_creator.recipe_is_stored(name_to_validate=name_request, recipe_inventory_list=recipe_inventory):
            return name_request
        else:
            raise exceptions.RecipeIsStored(f"A recipe with the name {name_request} is already stored.")

    @staticmethod
    def validate_menu_request(request, menu_list):
        if request in range(1, len(menu_list)+1):
            return request
        else:
            raise exceptions.MenuOptionInvalid("Your menu option is invalid. Try again...")

    def validate_ingredient_name(self, name_request, stored_values):
        if self.component_creator.ingredient_is_stored(name_to_validate=name_request, stored_values=stored_values):
            raise exceptions.IngredientIsStored(f"Ingredient with the the {name_request} is already stored.")
        else:
            return name_request

    @staticmethod
    def validate_save_request(request, options):
        if request in options:
            return request
        else:
            raise exceptions.InvalidSaveRequest("Your request is invalid.name")