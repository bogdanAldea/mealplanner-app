"""
MODULE DEFINES THE CHILD CLASS OF CONTROLLER THAT HANDLES RECIPE CREATIONS
"""
import controllers.controller as main
import models.recipe_model as recipe_model
import settings


class RecipeCreator(main.Controller):
    """
    Child class of Controller parent class that handles the creation of new recipes.
    Class uses the component selector & ingredient selector as tools.
    """

    def __init__(self, component_tools, ingredient_tools):
        """
        Constructor of recipe creator class.
        :param component_tools: object
        :param ingredient_tools: object
        """
        main.Controller.__init__(self)
        self.models = recipe_model.RecipeModel(settings.RECIPE_JSON_PATH)

        # selector tools
        self.components_tool = component_tools
        self.ingredients_tool = ingredient_tools

    def create(self):
        """
        Method allows user to create a new recipe from scratch, using the component data
        loaded from component data file.
        :return:
        """

        # screen rendering
        screen = self.views.creator_screens.CreateRecipeScreen()
        screen.render_screen()

        # display via the screen instance all the stored recipes(by name)
        stored_recipe_list = [recipe.get_name for recipe in self.models.recipe_data]

        try:
            # display all found recipes if the generated list of recipe name is not empty
            assert len(stored_recipe_list) > 0, "There are no recipes to display."
            screen.display_stored_recipes(stored_recipe_list)
        except AssertionError as e:
            screen.display_error(e)

        # define the id of the recipe
        ID = len(self.models.recipe_data) + 1

        # define recipe blueprint
        recipe_blueprint = self.models.get_recipe_blueprint

        # define ingredient set blueprint
        ingredient_set_blueprint = self.models.get_ingredient_set_blueprint

        # ask user to set a recipe name
        stored_recipes = [obj.get_name for obj in self.models.recipe_data]
        recipe_name = self.validate_recipe_name(stored_recipes)

        # define an empty list to which all ingredient sets are added
        ingredient_sets = list()

        # informative display of how the recipe is updated with new elements
        recipe_status = {
            "Recipe Name": recipe_name, "Recipe Ingredients": ingredient_sets
            }

        while True:

            # generate list of all component types to display as a menu
            component_types_list = list(self.components_tool.models.installed_components.keys())

            # select component and return its values
            selected_component, user_request = self.components_tool.get_component(component_types_list, recipe_status, sorting=False)

            # check if user's request is or is not a value for exit / back
            if user_request in ["q", "Q"]:
                break

            else:

                # select an ingredient from the returned list of values
                selected_ingredient, user_request = self.ingredients_tool.get_ingredient(selected_component, recipe_status)

                # check if user's request for ingredient selector is or is not a value for exit / back
                if user_request in ["q", "Q"]:
                    break

                else:

                    # set a quantity for selected ingredient
                    quantity = int(input(f"Set quantity for <{selected_ingredient}> >>> "))

                    # create a new ingredient set
                    new_set = ingredient_set_blueprint(selected_ingredient, quantity)

                    # add the new ingedient set to the define list from above.
                    ingredient_sets.append(new_set.__dict__)

        # put together elements that form the recipe
        new_recipe_object = recipe_blueprint(ID, recipe_name, ingredient_sets)

        # add the newly created recipe to the model recipe data.
        self.models.add_recipe(new_recipe_object)
        return new_recipe_object

    def save_recipe_data(self, recipe_object):
        """
        Method prompts user with option to update the model recipe data
        after a new recipe objects has been added.
        :param recipe_object: object
        :return: None
        """

        # render saving screen
        screen = self.views.save_screens.SaveRecipeScreen(recipe_object)
        screen.render_screen()

        while True:
            user_request = input("\nWant to save this recipe? >>> ")
            save_request, option_valid = self.validate_save_request(user_request)

            if option_valid:
                if save_request in ["n", "N"]:
                    break

                else:
                    self.models.save_recipe_data()
                    screen.confirmation_text()
                    break

            else:
                continue

