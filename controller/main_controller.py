from mealplanner_app.model.main_model import Model
from mealplanner_app.view.main_view import View
"""
Main controller module that implements views and models functionalities
"""


class Controller:

    def __init__(self, views, models):
        self.views = views
        self.models = models



