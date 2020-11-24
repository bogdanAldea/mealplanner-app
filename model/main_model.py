from mealplanner_app.model import json_backend
from mealplanner_app.model import editing_backend
from mealplanner_app.model import mealplanner_backend
from mealplanner_app.model import stocks_backend
from mealplanner_app.model import read_backend


"""
Main model module and business logic 
"""


class Model:

    def __init__(self):
        # SET PATH FOR EACH JSON FILE
        self.recipes_database = "D:/Coding/Coding/Projects/mealplanner/mealplanner_app/model/json_files/recipes.json"
        self.components_database = "D:/Coding/Coding/Projects/mealplanner/mealplanner_app/model/json_files/components.json"
        self.stocks_database = "D:/Coding/Coding/Projects/mealplanner/mealplanner_app/model/json_files/stocks.json"

        # GET DATA FROM EACH JSON FILE
        self.recipe_data = json_backend.read_json_from_file(json_file=self.recipes_database)  # dict
        self.components_data = json_backend.read_json_from_file(json_file=self.components_database)  # dict
        self.stocks_data = json_backend.read_json_from_file(json_file=self.stocks_database)  # dict

    def add_new_recipe(self) -> dict:
        NEW_RECIPE = editing_backend.create_new_recipe(recipe_components=self.components_data, loaded_json_data=self.recipe_data)
        return NEW_RECIPE

    def add_new_category_to_components(self) -> tuple:
        EDITED_COMPONENTS, EDITED_STOCKS = editing_backend.edit_components(components_data=self.components_data)
        return EDITED_COMPONENTS, EDITED_STOCKS

    def add_new_ingredient_to_components(self, menu) -> tuple:
        EDITED_COMPONENTS, EDITED_STOCKS = editing_backend.add_new_ingredient(components_data=self.components_data, stocks_data=self.stocks_data, menu_listing=menu)
        return EDITED_COMPONENTS, EDITED_STOCKS

    def update_recipe_data(self, new_recipe_data):
        UPDATED_DATA_TO_STORE = json_backend.update_json_data(current_data=self.recipe_data, new_data_to_store=new_recipe_data)
        json_backend.update_json_file(filename=self.recipes_database, updated_jso_data=UPDATED_DATA_TO_STORE)

    @staticmethod
    def update_single_data_set(old_data_set, new_data_set, datafile):
        UPDATED_DATA_SET = json_backend.update_json_data(current_data=old_data_set, new_data_to_store=new_data_set)
        json_backend.update_json_file(filename=datafile, updated_jso_data=UPDATED_DATA_SET)

    def update_multiple_data_sets(self, new_data_components, new_data_stocks):
        UPDATED_COMPONENTS_DATA = json_backend.update_json_data(current_data=self.components_data, new_data_to_store=new_data_components)
        UPDATED_STOCK_DATA = json_backend.update_json_data(current_data=self.stocks_data, new_data_to_store=new_data_stocks)
        json_backend.update_json_file(filename=self.components_database, updated_jso_data=UPDATED_COMPONENTS_DATA)
        json_backend.update_json_file(filename=self.stocks_database, updated_jso_data=UPDATED_STOCK_DATA)


