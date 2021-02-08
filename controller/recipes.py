"""
"""
import controller.selectors as selectors


class CreateRecipe(selectors.ComponentSelector, selectors.IngredientSelector):

    def __init__(self, VIEWS, MODELS):
        selectors.ComponentSelector.__init__(self, VIEWS=VIEWS, MODELS=MODELS)
        selectors.IngredientSelector.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def create(self):

        # refresh & clear screen / render recipe creation screen
        create_screen = self.views.main_screens.CreateRecipeScreen()
        create_screen.render_screen()

        # instance of recipe blueprint class
        recipe_blueprint = self.models.recipe_creator.get_recipe_blueprint()

        # recipe name variable
        recipe_name = self.validate_recipe_name()

        # recipe ingredients variable
        recipe_ingredients = dict()

        # recipe status (informative purpose)
        recipe_status = {
            "Recipe name": recipe_name,
            "Recipe Ingredients": recipe_ingredients
        }

        # components list for displaying as menu through views module
        components = self.models.component_creator.installed_components.keys()

        # start loop for component selection
        while True:

            # unpack returned values from component selector class
            selected_component, menu_request = self.get_component(components_list=components,
                                                                  recipe_status=recipe_status)

            # check if requested option is not a value for exit/back
            if menu_request not in ["q", "Q"]:

                # unpack values from ingredient selector class
                ingredient, quantity, menu_request = self.get_ingredient(ingredients_list=selected_component,
                                                                         recipe_status=recipe_status)

                # check if ingredient selector is not a values for exit/back
                if menu_request not in ["q", "Q"]:

                    # assemble ingredient-quantity pair
                    recipe_ingredients[ingredient] = quantity

            else:
                break

        # create recipe object with recipe blueprint using selected items
        recipe_object = recipe_blueprint(name=recipe_name, ingredients=recipe_ingredients)
        return menu_request, recipe_object

