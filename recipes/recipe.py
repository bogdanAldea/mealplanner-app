"""
MODULE DEFINES THE REPRESENTATION OF A RECIPE.
"""
import components.object_sets as obj_set


class Recipe:
    """
    Class represents a standard recipe described by:
    - an unique id, an unique name, a list of ingredients and their quantities.
    """

    def __init__(self, ID: int, obj_name: str, obj_ingredients: list):
        """
        Constructor of recipe class.
        :param ID: int
        :param obj_name: str
        :param obj_ingredients: list
        """

        self.ID: int = ID
        self.obj_name: str = obj_name

        # generates a list of ingredient set objects from given list of ingredients dicts.
        self.obj_ingredients: list = [obj_set.IngredientSet(**data) for data in obj_ingredients]

    # def __getitem__(self, item):
    #     return getattr(self, item)

    @property
    def get_id(self):
        return self.ID

    @property
    def get_name(self):
        return self.obj_name

    @property
    def get_ingredients(self):
        return self.obj_ingredients

    def __str__(self):
        return self.obj_name

    def export(self):
        """
        Method reverts the generated list of ingredient set objects to a list of dicts.
        This is used for json serialization.
        :return: list
        """
        ingredients_data_copy = self.obj_ingredients.copy()
        self.obj_ingredients.clear()
        self.obj_ingredients = [ingredients_data.__dict__ for ingredients_data in ingredients_data_copy]
        return self.__dict__