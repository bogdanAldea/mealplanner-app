"""
MODULE DESCRIBES EACH COMPONENT THAT REPRESENTS A TYPE OF INGREDIENT
"""


class Ingredient:

    def __init__(self, obj_name: str, obj_type: str = None):
        """
        Representation of the parent class ingredient.
        :param obj_name: name fo the ingredient
        :param obj_type: type of the ingredient (ex: Vegetable, Meat, Fruit etc...)
        """
        self.obj_name = obj_name

        if obj_type is None:
            self.obj_type = None
        else:
            self.obj_type = obj_type

    @property
    def get_name94(self) -> str:
        return self.obj_name

    @property
    def get_type(self) -> str:
        return self.obj_type


class Vegetable(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Vegetable"


class Meat(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Meat"


class Fruit(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Fruit"


class Flour(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Flour"


class Dairy(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Dairy"


class Seasoning(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Seasoning"


class Other(Ingredient):

    def __init__(self, obj_name: str):
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Other"