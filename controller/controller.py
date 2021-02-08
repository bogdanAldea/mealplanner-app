"""
"""
import models
import views


class Controller:

    exceptions = models.exceptions

    def __init__(self, VIEWS, MODELS):
        self.models: models.models = MODELS
        self.views: views = VIEWS

    """
    HELPER METHODS FOR HANDLING ERRORS    
    """

    def validate_recipe_name(self):

        # list of all recipes names already stored
        inventory = [recipe.get_name for recipe in self.models.recipe_creator.recipe_objects]

        # filter requested name and return if not found in inventory
        while True:
            try:
                requested_recipe_name = input("Set name >>> ")
                valid_name = self.models.validate_recipe_name(name_request=requested_recipe_name, recipe_inventory=inventory)
                return valid_name
            except Controller.exceptions.RecipeIsStored as e:
                self.views.display_error(e)

    def validate_save_request(self):
        options = ["y", "Y", "n", "N"]
        while True:
            try:
                save_request = input("\nWant to save your data? >>> ")
                valid_request = self.models.validate_save_request(request=save_request, options=options)
                return valid_request
            except Controller.exceptions.InvalidSaveRequest as e:
                self.views.display_error(e)

    def validate_menu_request(self, request, menu_options):
        while True:
            try:
                valid_menu_request = self.models.validate_menu_request(request, menu_options)
                return valid_menu_request, True
            except Controller.exceptions.MenuOptionInvalid as e:
                self.views.display_error(e)
                return None, False

    def validate_ingredient_name(self, component_values):
        try:
            requested_ingredient_name = input("Set ingredient name >>> ")
            valid_request = self.models.validate_ingredient_name(name_request=requested_ingredient_name, stored_values=component_values)
            return valid_request, True
        except Controller.exceptions.IngredientIsStored as e:
            self.views.display_error(e)
            return None, False

    """
    DATA SAVING METHODS FOR EACH MUTABLE OBJECT
    """

    def save_recipe(self, recipe_to_save):

        # refresh screen & render save screen
        save_screen = self.views.SaveRecipe(recipe_to_save)
        save_screen.render_screen()

        while True:
            try:
                request = self.validate_save_request()

                if request in ["y", "Y"]:
                    self.models.save_recipe(recipe_to_save)
                    save_screen.display_saving_status()

                elif request in ["n", "N"]:
                    break

                return request

            except Controller.exceptions.InvalidSaveRequest as e:
                self.views.display_error(e)
                continue

    def save_component(self):
        ...

    def save_ingredient(self):
        ...

    def save_inventory(self):
        ...

    """
    MAIN METHODS: CONTROLLER ACCEPTS REQUESTS FROM USERS THROUGH VIEWS CLASS
    AND RETRIEVES / UPDATES DATA THROUGH MODELS CLASS
    """

    def component_selector(self, components_list, recipe_status):

        # print menu to the screen via views class
        component_screen = self.views.ComponentSelector(components_list, recipe_status)
        component_screen.render_screen()

        # get user request for component selection
        while True:
            selector_request = input("\nSelect component >>> ")

            # check if request is a value of exit/break
            if selector_request in ["q", "Q"]:
                return None, selector_request

            else:
                valid_request, flag = self.validate_menu_request(request=int(selector_request), menu_options=components_list)
                if flag:
                    ingredient_values = self.models.component_creator.select_component_values(request=int(valid_request))
                    return ingredient_values, selector_request

                else:
                    continue

    def ingredient_selector(self, ingredients_list, recipe_status):

        # print menu to the screen via views class
        ingredient_screen = self.views.IngredientSelector(ingredient_menu_list=ingredients_list,recipe_status=recipe_status)
        ingredient_screen.render_screen()

        # check if request is value of exit/back
        while True:

            selector_request = input("\nSelect ingredient >>> ")

            # check if request is a value of exit/back
            if selector_request in ["q", "Q"]:
                return None, None, selector_request

            else:
                valid_request, flag = self.validate_menu_request(request=int(selector_request), menu_options=ingredients_list)
                if flag:
                    selected_ingredient = self.models.component_creator.select_from_values(request=int(selector_request),
                                                                                           values=ingredients_list)
                    selected_quantity = int(input("Quantity >>> "))
                    return selected_ingredient, selected_quantity, selector_request

                else:
                    continue

    """
    METHOD IMPLEMENTS FUNCTIONALITY FOR CREATING A BRAND NEW RECIPE
    - SELECTS COMPONENT
    - SELECTS INGREDIENTS & QUANTITIES
    """
    def create_recipe(self):

        # refresh and clear screen / render create recipe screen
        screen = self.views.Create_Recipe()
        screen.render_screen()

        # recipe blueprint class instance
        recipe_blueprint = self.models.recipe_creator.get_recipe_blueprint()

        # recipe name var
        recipe_name = self.validate_recipe_name()

        # recipe ingredients var
        recipe_ingredients = dict()

        # recipe status (informative purpose)
        recipe_status = {
            "Recipe name": recipe_name,
            "Recipe ingredients": recipe_ingredients}

        # components list for views to display as menu
        components = self.models.component_creator.installed_components.keys()

        # start loop
        while True:

            # unpack returned values from component_selector method
            selected_component, menu_request = self.component_selector(components_list=components,
                                                                       recipe_status=recipe_status)

            # check if requested option is not a value for exit/back
            if menu_request not in ["q", "Q"]:

                # unpack values from ingredient_selector method
                ingredient, quantity, menu_request = self.ingredient_selector(ingredients_list=selected_component,
                                                                              recipe_status=recipe_status)

                # check if ingredient request is not a value of exit/back
                if menu_request not in ["q", "Q"]:

                    # assemble ingredient-quantity pair
                    recipe_ingredients[ingredient] = quantity

            else:
                break

        # create recipe object using selected items & recipe blueprint
        recipe_object = recipe_blueprint(name=recipe_name, ingredients=recipe_ingredients)
        return menu_request, recipe_object

    """
    METHOD IMPLEMENTS FUNCTIONALITY FOR CREATING A NEW INGREDIENT
    - CREATES INGREDIENT & SORTS IT BASED ON COMPONENT SELECTED
    """
    def create_ingredient(self, request, stored_ingredients):

        # refresh screen/render ingredient creation screen
        create_ingredient_screen = self.views.NewIngredient()
        create_ingredient_screen.render_screen()

        while True:
            # set ingredient name
            ingredient_name, flag = self.validate_ingredient_name(component_values=stored_ingredients)

            if flag:
                # create ingredient object with component creator matrix
                ingredient_object = self.models.component_creator.create_component(component_name=ingredient_name, request=request)
                return ingredient_object

            else:
                continue

    """
    METHOD ALLOWS FOR CREATING & ADDING NEW INGREDIENTS
    - SELECTS COMPONENT TO ADD INGREDIENTS TO
    - SORTS NEWLY ADDED INGREDIENT TO ITS SELECTED COMPONENT
    """
    def add_new_ingredient(self):

        # components list for views to display as menu
        components = self.models.component_creator.installed_components.keys()

        while True:
            # select component to add ingredient to
            component_values, component_selector = self.component_selector(components_list=components,
                                                                           recipe_status=None)

            # check if component selector is not a value for quit.back
            if component_selector not in ["q", "Q"]:

                # create new ingredient
                ingredient_object = self.create_ingredient(request=int(component_selector),
                                                           stored_ingredients=component_values)

                # sort newly created ingredient to its specific component
                self.models.component_creator.sort_component(new_component=ingredient_object)
                return component_selector

            else:
                break
