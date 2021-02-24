"""
MODULE DEFINES CLASSES THAT REPRESENTS A PAIR / SET OF:
- COMPONENTS -> DESCRIBED BY TYPE AND AN COLLECTION AN VALUES
- INGREDIENTS -> DESCRIBED BY A NAME AND A GIVEN QUANTITY
"""


class ComponentsSet:
    """
    Class represents an object set defined by its given type and its specific values.
    Ex: Type: Fruit, Items: list of fruit names.
    """

    def __init__(self, obj_type: str, obj_items: list):
        """
        Constructor of component set class.
        :param obj_type: str
        :param obj_items: list
        """
        self.obj_type: str = obj_type
        self.obj_items: list = obj_items

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def get_obj_type(self) -> str:
        return self.obj_type

    @property
    def get_obj_items(self) -> list:
        return self.obj_items

    def export_dict(self) -> dict:
        """
        Method returns a dict version of the object used for json serialization.
        :return: dict
        """
        return self.__dict__


class IngredientSet:
    """
    Class represents an object set defined by a name and a quantity.
    Ex: Name: Apple, Quantity: 1
    """

    def __init__(self, name: str, quantity: int):
        """
        Constructor of ingredient set class.
        :param name: str
        :param quantity: int
        """
        self.name = name
        self.quantity = quantity

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def get_name(self):
        return self.name

    @property
    def get_quantity(self):
        return self.quantity

    def set_quantity(self, value) -> None:
        self.quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    def export_dict(self) -> dict:
        """
        Method returns a dict version of the objects for json serialization.
        :return: dict
        """
        return self.__dict__