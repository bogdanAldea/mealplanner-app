"""
MODULE DEFINES THE REPRESENTATION OF AN RECIPE AND ITS ELEMENTS
"""
import components.object_sets as Set


class Recipe:

    def __init__(self, ID: int, obj_name: str, obj_ingredients: list):
        """
        CLASS DESCRIBES THE REPRESENTATION OF AN RECIPE OBJECT
        :param ID: unique id number
        :param obj_name: unique str
        :param obj_ingredients: list of dictionaries representing the name-quantity pair
        """
        self.ID = ID
        self.obj_name = obj_name
        self.obj_ingredients = [Set.IngredientSet(**data) for data in obj_ingredients]

    @property
    def get_name(self):
        return self.obj_name

    @property
    def get_ingredients(self):
        return self.obj_ingredients

    def convert_for_export(self):
        """
        METHOD TAKES EACH INGREDIENT_SET ITEM FROM THE LIST OF INGREDIENTS AND CONVERT THEM
        TO A DICT. THIS ALLOWS FOR THE RECIPE OBJECT TO BE CONVERTED TO A DICT AND STORED INSIDE A JASON FILE
        :return: list of dict
        """
        ingredient_data = self.obj_ingredients.copy()
        self.obj_ingredients.clear()
        self.obj_ingredients = [data.export() for data in ingredient_data]
        return self.__dict__


