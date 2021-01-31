"""
"""
import mealplanner_app.recipe.recipe_manager as recipe_manager
import mealplanner_app.recipe.recipe as recipe


class RecipeCreator(recipe_manager.RecipeManager):

    def __init__(self, database_path):
        recipe_manager.RecipeManager.__init__(self, database_path)
        self.recipe_matrix = recipe.Recipe
        self.recipe_objects = [self.recipe_matrix(**recipe_data) for recipe_data in self.loaded_data]

    @staticmethod
    def recipe_is_stored(name_to_validate: str, recipe_inventory_list: list) -> bool:
        if name_to_validate in recipe_inventory_list:
            return False
        else:
            return True

    def set_recipe_name(self, name: str, recipe_inventory_list: list) -> str:
        if self.recipe_is_stored(name_to_validate=name, recipe_inventory_list=recipe_inventory_list):
            return name
        else:
            raise BaseException  # temporary exception