from mealplanner_app.model.main_model import Model
from mealplanner_app.view.main_view import View
"""
Main controller module that implements views and models functionalities
"""


class Controller:

    def __init__(self):
        self.views = View()
        self.models = Model()

    def add_new_recipe(self):
        available_recipes = self.models.read_recipe_items()
        self.views.show_items_menu(list_items=available_recipes, title="Retete salvate", display_bullet_points=True)
        new_recipe = self.models.add_new_recipe()
        self.models.update_recipe_data(new_recipe_data=new_recipe)

    def add_new_category_to_components(self):
        available_categories = self.models.read_components_items()
        self.views.show_items_menu(list_items=available_categories, title="Categorii existente", display_bullet_points=True)
        edited_components, edited_stocks = self.models.add_new_category_to_components()
        self.models.update_multiple_data_sets(new_data_components=edited_components, new_data_stocks=edited_stocks)

    def add_new_ingredients_to_category(self):
        available_categories = self.models.read_components_items()
        self.views.show_items_menu(list_items=available_categories, title="Categorii existente", display_bullet_points=False)
        edited_component, edited_stocks = self.models.add_new_ingredient_to_components(menu=available_categories)
        self.models.update_multiple_data_sets(new_data_components=edited_component, new_data_stocks=edited_stocks)

    def create_new_mealplan(self):
        available_recipes = self.models.read_recipe_items()
        self.views.show_items_menu(list_items=available_recipes, title="Retete salvate", display_bullet_points=False)
        shopping_cart, edited_stocks = self.models.create_new_mealplan(menu=available_recipes)
        self.models.update_single_data_set(old_data_set=self.models.stocks_data, new_data_set=edited_stocks, datafile=self.models.stocks_database)
        self.models.write_shopping_cart(mealplan_cart=shopping_cart)









