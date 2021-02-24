"""

"""
import views.screen


class CreateRecipeScreen(views.screen.Screen):

    def __init__(self):
        views.screen.Screen.__init__(self)
        self.title = "Create new recipe"
        self.info = "There are many variations of passages of Lorem Ipsum available, but the " \
                    "majority have suffered alteration in some form, by injected humour"

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()

    @staticmethod
    def display_stored_recipes(recipe_list: list, as_bullet_point=True):
        print("===== STORED RECIPES =====")
        if as_bullet_point:
            for recipe in recipe_list:
                print(f"* {recipe}")
        else:
            for index, recipe in enumerate(recipe_list):
                print(f"{[index+1]} {recipe}")
