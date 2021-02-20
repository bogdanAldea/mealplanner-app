"""
MODULE DEFINES CLASSES THAT REPRESENTS TYPES OF INGREDIENTS USED TO
CREATE RECIPES.
"""


class Ingredient:
    """
    Parent class that defines the representation of an ingredient.
    """

    def __init__(self, obj_name: str, obj_type: str = None):
        """
        Constructor of parent class. 

        :param obj_name: str
        :param obj_type: str
        """
        if obj_type is None:
            self.obj_type = str()
        else:
            self.obj_type = obj_type
        self.obj_name: str = obj_name

    @property
    def name(self):
        return self.obj_name

    @property
    def type(self):
        return self.obj_type


class Vegetable(Ingredient):
    """
    Child class of Ingredient class. Represents Vegetable component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Vegetable class.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Vegetable"


class Meat(Ingredient):
    """
    Child class of Ingredient class. Represents Meat component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Meat class.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Meat"


class Dairy(Ingredient):
    """
    Child class of Ingredient class. Represents Dairy component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Dairy class.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Dairy"


class Fruit(Ingredient):
    """
    Child class of Ingredient class. Represents Fruit component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Fruit component.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Fruit"


class Flour(Ingredient):
    """
    Child class of Ingredient class. Represents Flour component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Flour component.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Flour"


class Seasoning(Ingredient):
    """
    Child class of Ingredient class. Represents Seasoning component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Seasoning class.
        :param obj_name: str
        """

        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Seasoning"


class Other(Ingredient):
    """
    Child class of Ingredient class. Represents Other component.
    """

    def __init__(self, obj_name: str):
        """
        Constructor of Other class.
        :param obj_name: str
        """
        Ingredient.__init__(self, obj_name=obj_name)
        self.obj_type = "Other"