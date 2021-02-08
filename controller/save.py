"""
"""

import controller.main_controller as main


class SaveRecipe(main.Controller):

    def __init__(self, VIEWS, MODELS):
        main.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def save(self, recipe_to_save):

        # refresh & clear screen / render save recipe screen
        save_screen = self.views.save_screens.SaveRecipeScreen(recipe_to_save)
        save_screen.render_screen()

        while True:
            try:
                save_request = self.validate_save_request()

                # check is request is for saving
                if save_request in ["y", "Y"]:

                    # save recipe data to db
                    self.models.save_recipe(recipe_to_save)
                    save_screen.display_saving_status()

                elif save_request in ["n", "N"]:
                    break

                return save_request

            except main.Controller.exceptions.InvalidSaveRequest as e:
                save_screen.display_error_message(e)
                continue


class SaveComponent(main.Controller):

    def __init__(self, VIEWS, MODELS):
        main.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def save(self):
        ...


class SaveIngredient(main.Controller):

    def __init__(self, VIEWS, MODELS):
        main.Controller.__init__(self, VIEWS=VIEWS, MODELS=MODELS)

    def save(self):
        ...