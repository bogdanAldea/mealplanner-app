"""
MODULE IMPLEMENTS INVENTORY CLASS.
"""
import components.object_sets as obj_sets


class Inventory:
    """
    Class defines an inventory item described by a type and list of ingredient sets.
    Ex: object type: "Fruit", object item: list of {"name": ..., "quantity": x}
    """

    def __init__(self, obj_type: str, obj_items: list):
        """
        Constructor of inventory class.
        :param obj_type: str
        :param obj_items: list
        """
        self.obj_type = obj_type

        # generates a list of ingredient sets from given list of dicts
        self.obj_items = [obj_sets.IngredientSet(**data) for data in obj_items]

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def get_type(self):
        return self.obj_type

    @property
    def get_items(self):
        return self.obj_items

    def add_new(self, ingredient_set):
        if isinstance(ingredient_set, list):
            self.obj_items.extend(ingredient_set)
        else:
            self.obj_items.append(ingredient_set)

    def export(self):
        """
        Method reverts list of ingredient sets back to list of dicts and returns an
        dict version on entire object. This is used for json serialization.
        :return: dict
        """
        
        inventory_items_copy = self.obj_items.copy()
        self.obj_items.clear()
        self.obj_items = [item.__dict__ for item in inventory_items_copy]
        return self.__dict__