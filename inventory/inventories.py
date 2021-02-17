"""
MODULE DEFINES THE DESCRIPTION OF AN INVENTORY
"""
import components.object_sets as SET


class Inventory:

    def __init__(self, obj_type: str, obj_items: list):
        """

        :param obj_type:
        :param obj_items:
        """

        self.obj_type = obj_type
        self.obj_items = [SET.IngredientSet(**data) for data in obj_items]

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def get_type(self) -> str:
        return self.obj_type

    @property
    def get_items(self) -> list:
        return self.obj_items

    def add_new(self, new_ingredient_set: SET.IngredientSet) -> None:
        """
        METHOD ADDS A NEW INGREDIENT SET TO THE LIST BASED OF ITS SPECIFIC TYPE
        :param new_ingredient_set: obj of class IngredientSet
        :return: None
        """
        if isinstance(new_ingredient_set, list):
            self.obj_items.extend(new_ingredient_set)
        else:
            self.obj_items.append(new_ingredient_set)