"""
"""

import controller.main_controller as controller


class ComponentSelector(controller.Controller):

    def __init__(self, VIEWS, MODELS):
        controller.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def get_component(self, components_list, recipe_status=None):

        # refresh & clear screen / render component selection screen
        component_screen = self.views.selector_screens.ComponentSelector(components_list, recipe_status)
        component_screen.render_screen()

        # get user request for component selection
        while True:
            selector_request = input("\nSelect component >>> ")

            # check if request is a value of exit/break
            if selector_request in ["q", "Q"]:
                return None, selector_request

            else:
                # validate request as an menu option
                valid_request, flag = self.validate_menu_request(request=int(selector_request),
                                                                 menu_options=components_list)

                if flag:

                    # return values from selected component dict
                    ingredient_values = self.models.component_creator.select_component_values(request=int(valid_request))
                    return ingredient_values, selector_request

                else:
                    continue


class IngredientSelector(controller.Controller):

    def __init__(self, VIEWS, MODELS):
        controller.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def get_ingredient(self, ingredients_list, recipe_status=None):

        # refresh & clear screen / render component selection screen
        ingredient_screen = self.views.selector_screens.IngredientSelector(ingredients_list, recipe_status)
        ingredient_screen.render_screen()

        # get user request for component selection
        while True:
            selector_request = input("\nSelect ingredient >>> ")

            # checks if request is a values of exit/back
            if selector_request in ["q", "Q"]:
                return None, None, selector_request

            else:
                # validate request as an menu option
                valid_request, flag = self.validate_menu_request(request=int(selector_request),
                                                                 menu_options=ingredients_list)

                if flag:

                    # return specific list item from component values based on the selector request
                    selected_ingredient = self.models.component_creator.select_from_values(request=int(selector_request),
                                                                                           values=ingredients_list)

                    # assign a quantity value to the selected ingredient
                    selected_quantity = int(input("Quantity >>> "))

                    return selected_ingredient, selected_quantity, selector_request

                else:
                    continue