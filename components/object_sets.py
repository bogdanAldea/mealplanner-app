"""
MODULE DEFINES WHAT A COMPONENT SET AND AN INGREDIENT SET ARE
ALLOWS FOR EASIER MANIPULATION OF MORE COMPLEX OBJECTS
"""


class ComponentSet:

    def __init__(self, obj_type: str, obj_items: list):
        """
        CLASS DESCRIBES AN OBJECT DEFINED BY A TYPE (MEAT, VEGETABLE ETC...) ALONG WITH ITS VALUES
        :param obj_type: str determined by the type of its basic component
        :param obj_items: list of values specific for their component type
                          (ex: for the type "Vegetable" -> values = ["carrot", "onion" etc])
        """
        self.obj_type: str = obj_type
        self.obj_items: list = obj_items

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def get_type(self) -> str:
        return self.obj_type

    @property
    def get_items(self) -> list:
        return self.obj_items


class IngredientSet:

    def __init__(self, obj_name: str, obj_quantity: int):
        """
        CLASS REPRESENT AN UNIQUE SET/PAIR OF INGREDIENTS AND THEIR QUANTITIES
        :param obj_name: str given by user/selection
        :param obj_quantity: number >= 0
        """
        self.obj_name: str = obj_name
        self.obj_quantity: int = obj_quantity

    def __getitem__(self, item):
        return getattr(self, item)

    def set_quantity(self, new_value: int) -> None:
        self.obj_quantity = new_value