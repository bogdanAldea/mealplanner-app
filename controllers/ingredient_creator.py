"""
MODULE HANDLES THE CREATION OF NEW INGREDIENT OBJECTS.
"""
import controllers.component_selector as component_selector


class CreateIngredient(component_selector.ComponentSelector):
    """
    Class inherits the component selector class.

    Class creates a new ingredient objects by allowing user to select his desired
    component type ("meat", "vegetable", "dairy" etc.).
    """

    def __init__(self):
        """
        Constructor of ingredient creation class.
        """
        component_selector.ComponentSelector.__init__(self)

    def create_new(self):
        """
        Main method that handles the creation of a new ingredient. Context required the ingredient
        to be sorted into the component data file, so get_component method is allowed
        to return an empty list of values.

        Method returns the created ingredient to be sort into the inventory data file.

        :return: object
        """

        # START LOOP
        while True:

            # prompt user to select component type and return its list of values
            component_types_list = list(self.models.installed_components.keys())
            selected_values, user_request = self.get_component(component_types_list, recipe_status=None, sorting=True)

            # check if user's request is or is not a values for exit / back
            if user_request in ["q", "Q"]:
                break

            else:
                while True:

                    # set a name for the ingredient
                    ingredient_name = input("\nSet name >>> ")

                    # create ingredient object
                    ingredient_object = self.models.new_ingredient(ingredient_name, int(user_request))

                    # attempt sorting the ingredient
                    ingredient_not_found = self.sort(ingredient_object, selected_values)

                    # when sorting is attempted, if ingredient was not already stored
                    # program exits
                    if ingredient_not_found:
                        return ingredient_object
                    else:
                        break