"""
MODULE DEFINES THE MODEL CHILD CLASS THAT HANDLES
ALL INVENTORY RELATED BUSINESS LOGIC
"""
import models.model as main
import inventories.inventory as inventory
import components.object_sets as obj_sets
import json_db


class InventoryModel(main.Model):
    """
    Child class of Model that handles data manipulation and business logic of inventory
    json file.
    """

    def __init__(self, inventory_json_file):
        """
        Constructor of inventory model class.

        :param inventory_json_file: file path
        """
        main.Model.__init__(self)

        # path of inventory json file
        self.database_file = inventory_json_file

        # temp variable with loaded data from component json file
        temp_file_data = json_db.load_file(self.database_file)

        # generated list of inventory objects from dictionaries read from json file
        self.inventory_data = [inventory.Inventory(**data) for data in temp_file_data]

    def get_item(self, item_type: str) -> list:
        """
        Method returns requested item values based on requested type
        :param item_type: str
        :return: Inventory object
        """
        target_item: inventory.Inventory = next(item for item in self.inventory_data if item["obj_type"] == item_type)
        return target_item

    def sort_ingredient(self, new_ingredient):
        """
        Method takes a newly created ingredient as sorts it into its respective list
        based on its type
        :param new_ingredient: INGREDIENT OBJECT
        :return: None
        """

        # filter list of data and return requested list using given ingredient's type
        target_item: inventory.Inventory = self.get_item(new_ingredient.get_type)

        # create new ingredient set with default quantity of 0
        ingredient_set = obj_sets.IngredientSet(new_ingredient.get_name, quantity=0)

        # append ingredient set to returned list
        target_item.add_new(ingredient_set)

    def save_inventory_data(self):
        """
        Methods save updated inventory data to json file
        :return: None
        """

        # convert inventory object items into dictionaries for json serialization
        updated_inventory_data = [data.export() for data in self.inventory_data]

        # save inventory data to json file
        json_db.save_file(updated_inventory_data, self.database_file)