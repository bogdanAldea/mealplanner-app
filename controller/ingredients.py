"""
"""

import controller.main_controller as main
import controller.selectors as selector


class CreateIngredient(main.Controller):

    def __init__(self, VIEWS, MODELS):
        main.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def create_new(self, request, stored_ingredients):

        # refresh & clear screen / render ingredient creation screen
        create_ingredient_screen = self.views.creator_screens.NewIngredient()
        create_ingredient_screen.render_screen()

        while True:

            # set ingredient name
            ingredient_name, flag = self.validate_ingredient_name(component_values=stored_ingredients)

            # check if the new ingredients exists or not
            if flag:

                # if ingredient does not exist, start creation
                ingredient_object = self.models.component_creator.create_component(component_name=ingredient_name,
                                                                                   request=int(request))
                return ingredient_object

            else:
                # if ingredient exists -> exception will be raised
                continue


class AddNewIngredient(CreateIngredient, selector.ComponentSelector):

    def __init__(self, VIEWS, MODELS):
        selector.ComponentSelector.__init__(self, MODELS=MODELS, VIEWS=VIEWS)
        CreateIngredient.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def add(self):

        # components list for views to display as menu
        components = self.models.component_creator.installed_components.keys()

        while True:

            # select component to add new ingredients to
            component_values, component_menu_selector = self.get_component(components_list=components)

            # check if component selector is not a value for exit/back
            if component_menu_selector not in ["q", "Q"]:

                # create new ingredient
                ingredient_object = self.create_new(request=int(component_menu_selector),
                                                    stored_ingredients=component_values)

                # sort newly created ingredient to its specific type of component
                self.models.component_creator.sort_component(new_component=ingredient_object)

                return component_menu_selector

            else:
                break