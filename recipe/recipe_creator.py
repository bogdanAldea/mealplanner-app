"""
"""
from recipe.recipe import Recipe
from recipe import recipe_manager


class RecipeCreator(recipe_manager.RecipeManager):

    def __init__(self, database_path):
        recipe_manager.RecipeManager.__init__(self, database_path)
        self.recipe_matrix = Recipe
        self.recipe_objects = [self.recipe_matrix(**recipe_data) for recipe_data in self.loaded_data]

    @staticmethod
    def recipe_is_stored(name_to_validate: str, recipe_inventory_list: list) -> bool:
        if name_to_validate in recipe_inventory_list:
            return False
        else:
            return True

    def get_recipe_blueprint(self) -> object:
        return self.recipe_matrix

