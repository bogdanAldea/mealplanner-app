"""
MODULE DEFINES MODEL CHILD CLASS THAT HANDLES
ALL RECIPE RELATED BUSINESS LOGIC
"""
import models.model as main
import recipes.recipe as recipe
import components.object_sets as obj_sets
import json_db


class RecipeModel(main.Model):
    """
    Class inherits parent class Model and handles business logic of recipe data.
    """

    def __init__(self, recipe_json_file):
        """
        Constructor of recipe model class.
        :param recipe_json_file: file path of recipe json file
        """

        main.Model.__init__(self)
        self.database_file = recipe_json_file

        # temp variable that stores data from recipe json file after being read.
        temp_file_data = json_db.load_file(self.database_file)

        # generate list of recipe objects from loaded list of dictionaries from json file
        self.recipe_data = [recipe.Recipe(**data) for data in temp_file_data]

    @property
    def get_recipe_blueprint(self):
        return recipe.Recipe

    @property
    def get_ingredient_set_blueprint(self):
        return obj_sets.IngredientSet

    def add_recipe(self, new_recipe: recipe.Recipe) -> None:
        """
        Method appends a newly created recipe object to list of data.
        :param new_recipe: object
        :return: None
        """

        self.recipe_data.append(new_recipe)

    def save_recipe_data(self) -> None:
        """
        Method writes recipe data as list of dictionaries to its assigned json file.
        :return: None
        """

        # generated list of each recipe item from self.recipe_data as dict
        data_to_save = [obj.export() for obj in self.recipe_data]
        json_db.save_file(data_to_save, self.database_file)