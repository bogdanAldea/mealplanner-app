"""
MODULE DEFINES THE MODEL CHILD CLASS THAT HANDLES
ALL COMPONENT RELATED BUSINESS LOGIC
"""
import json_db
import models.model
import components.object_sets as obj_sets
import components.ingredients as ingredients


class ComponentModel(models.model.Model):
    """
    Child class of Model class. Describes business logic of components / ingredients data
    and interaction with json files(database).
    """

    def __init__(self, component_json_file):
        """
        Constructor of component model class
        :param component_json_file:
        """
        models.model.Model.__init__(self)

        # path of component json file
        self.database_file = component_json_file

        # temp variable with loaded data from component json file
        temp_file_data = json_db.load_file(self.database_file)

        # generate with of component sets from dictionaries loaded form component json data
        self.component_data = [obj_sets.ComponentsSet(**data) for data in temp_file_data]

    @property
    def get_component_data(self):
        return self.component_data

    def get_component_blueprint(self, request: int):
        """
        Method returns the desired component class based on user request
        :param request:
        :return: class
        """

        # list of keys representing type of all components
        installed_components_keys: list = list(self.installed_components.keys())

        selected_key = installed_components_keys[request-1]

        # returned component class
        return self.installed_components.get(selected_key)

    @staticmethod
    def get_ingredient_set_blueprint():
        """
        Method returns ingredient set class
        :return: class
        """
        return obj_sets.IngredientSet

    def new_ingredient(self, ingredient_name: str, request: int) -> ingredients.Ingredient:
        """
        Method creates new ingredient object with selected component class
        :param ingredient_name: str
        :param request: int
        :return: object
        """
        selected_blueprint = self.get_component_blueprint(request)
        return selected_blueprint(ingredient_name)

    def filter_values(self, component_type: str, sorting=False) -> list:
        """
        Method filters list of component objects read from json file and returns values of
        selected component based on user request.

        When values list is returned, it is possible that the respective list may be empty.
        Based on this method's usage, the sorting attr (used for sorting new ingredients into
        their specific list of values) may or may not allow the return of an
        empty list.

        :param component_type: str
        :param sorting: bool
        :return: list
        """

        # check if methods is used for sorting new ingredients
        if sorting is False:

            try:
                # return values that will only match the component's type AND is not an empty list
                target_items = next(item["obj_items"] for item in self.component_data
                                    if item["obj_type"] == component_type
                                    and len(item["obj_items"]) > 0)
                return target_items

            except StopIteration:
                # if list matched by type is empty, raise exception
                raise ComponentModel.exceptions.EmptyListOfValues(f"Component <{component_type}> has no values.")

        else:
            # if method is user for sorting new ingredient objects, return list (empty ot not)
            target_items = next(item["obj_items"] for item in self.component_data
                                if item["obj_type"] == component_type)
            return target_items

    @staticmethod
    def sort_ingredient(new_ingredient: ingredients.Ingredient, target_values) -> None:
        """
        Method takes a new ingredient object as parameter and puts it in its respective list.
        Before it is appended, method checks if the ingredient's name has a match inside its respective list.
        :param new_ingredient: ingredient object
        :param target_values: list
        :return: None
        """

        # compare ingredient's name with elements of target_values list:
        if new_ingredient.name not in target_values:

            # if string was not found inside the target list, append string
            target_values.append(new_ingredient.name)

        else:
            # raise exception if there is a match
            raise ComponentModel.exceptions.IngredientIsStored(
                f"An ingredient with the name <{new_ingredient.name}> is already stored.")

    @staticmethod
    def select_from_values(request: int, values: list) -> str:
        return values[request-1]

    def save_component_data(self) -> None:
        """
        Method takes list of component objects and saves it into component json file
        :return: None
        """
        data_to_save = [comp.__dict__ for comp in self.component_data]
        json_db.save_file(data_to_save, self.database_file)