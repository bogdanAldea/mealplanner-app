"""

"""
import views.creator_screens as create_screen
import termcolor
import time


class SaveRecipeScreen(create_screen.CreateRecipeScreen):

    def __init__(self, recipe_to_save):
        create_screen.CreateRecipeScreen.__init__(self)
        self.title = "Save recipe"
        self.info = ""
        self.recipe_to_save = recipe_to_save

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
        self.display_recipe_info()

    def display_recipe_info(self):
        info_text = f"\nRecipe has been created:\n" \
                    f"Name              >>> {self.recipe_to_save.get_name}\n" \
                    f"Ingredients       >>> {[x.__dict__ for x in self.recipe_to_save.get_ingredients]}"
        print(info_text)

    @staticmethod
    def confirmation_text():
        confirm_status = termcolor.colored(text="\nRecipe saved successfully", color="green")
        print(confirm_status)
        time.sleep(2)