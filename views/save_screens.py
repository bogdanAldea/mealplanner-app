"""
"""
import views.screen_manager as screen_manager
import termcolor
import time


class SaveRecipeScreen(screen_manager.ScreenManager):

    def __init__(self, recipe_to_save):
        screen_manager.ScreenManager.__init__(self)
        self.title = f"Save Recipe ({recipe_to_save.get_name})"
        self.info_panel = str()
        self.recipe_to_save = recipe_to_save

    def display_recipe_info(self):
        info_text = f"\nRecipe has been created:\n" \
                    f"Name              >>> {self.recipe_to_save.get_name}\n" \
                    f"Ingredients       >>> {self.recipe_to_save.get_ingredients}"
        print(info_text)

    @staticmethod
    def display_saving_status():
        text_info = termcolor.colored(text="Data is being saved. Please wait...", color='green')
        confirmation = termcolor.colored(text="Data was saved successfully.", color="green")

        print(text_info)
        time.sleep(2)
        print(confirmation)
        time.sleep(2)

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
        self.display_recipe_info()


class SaveIngredientScreen(screen_manager.ScreenManager):

    def __init__(self, new_value: str, values: list):
        screen_manager.ScreenManager.__init__(self)
        self.title = "Save Ingredient"
        self.info_panel = str()
        self.new_value = new_value
        self.updated_values = values

    def display_values(self):
        for value in self.updated_values:
            highlight = value
            if highlight == self.new_value:
                highlight = termcolor.colored(text=value, color='green')
            print(highlight)

    def render_screen(self):
        screen_manager.ScreenManager().render_screen()
        self.display_values()


