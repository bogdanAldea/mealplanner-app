"""
"""


class Recipe:

    def __init__(self, name: str, ingredients: dict):
        self.name: str = name
        self.ingredients: dict = ingredients

    @property
    def get_name(self):
        return self.name

    @property
    def get_ingredients(self):
        return self.ingredients