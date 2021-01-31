"""
"""


class Component:

    def __init__(self, name: str):
        self.name: str = name
        self.type = str()

    @property
    def get_name(self):
        return self.name

    @property
    def get_type(self):
        return self.type


class Meat(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Meat"


class Vegetable(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Vegetable"


class Dairy(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Dairy"


class Fruit(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Fruit"


class Flour(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Flour"


class Other(Component):
    def __init__(self, name: str):
        Component.__init__(self, name)
        self.type = "Other"


class Custom(Component):
    def __init__(self, name: str, TYPE: str):
        Component.__init__(self, name)
        self.type = TYPE

