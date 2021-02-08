"""
"""
from pyfiglet import figlet_format
import termcolor
import textwrap
import os
import time


class Screen:

    def __init__(self):
        self.title = "Mealplanner App"
        self.info = str()
        self.menu = list()
        self.recipe_status = dict()

    def render_screen(self):
        self.refresh_screen()
        self.display_logo()
        self.display_info()
        self.display_menu()

    @staticmethod
    def display_error(exception_error: Exception):
        error_text = termcolor.colored(text=exception_error.args[0], color='red')
        print(error_text)

    def display_info(self):
        info_text = textwrap.fill(text=self.info, width=60)
        info_text = termcolor.colored(text=info_text, color='cyan')
        print(info_text+"\n")

    def display_logo(self):
        title = figlet_format(text=self.title)
        print(title)

    def display_menu(self):
        for idx, item in enumerate(self.menu):
            menu_line = f"[{idx+1}] {item}"
            print(menu_line)

    def display_recipe_status(self):

        if self.recipe_status is not None:

            # unpack dictionary keys & values
            field_a, field_b = list(self.recipe_status.keys())
            content_a, content_b = list(self.recipe_status.values())

            # add color and formatting to keys
            field_a = termcolor.colored(text=field_a.upper(), color="green")
            field_b = termcolor.colored(text=field_b.upper(), color="green")

            # print status to the screen
            status = f"{field_a}: {content_a}\n{field_b}: {content_b}"
            print(status)

        else:
            return None

    @staticmethod
    def refresh_screen():
        os.system('cls')


class MainScreen(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.title = "Main Menu"
        self.info = ""
        self.menu = \
            [
                "Mealplanner",
                "Add new recipe",
                "Add new component",
                "Add ingredient to component"
            ]


class Mealplanner(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.info = ""


class Create_Recipe(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.title = "Create Recipe"
        self.info = "There are many variations of passages of Lorem Ipsum available, but the " \
                    "majority have suffered alteration in some form, by injected humour"


class ComponentSelector(Create_Recipe):
    def __init__(self, components_menu_list, recipe_status):
        Create_Recipe.__init__(self)
        self.title = "Select component"
        self.info = "It is a long established fact that a reader will be distracted by " \
                    "the readable content of a page when looking at its layout."
        self.menu = components_menu_list
        self.recipe_status = recipe_status

    def render_screen(self):
        self.refresh_screen()
        self.display_logo()
        self.display_info()
        self.display_recipe_status()
        self.display_menu()


class IngredientSelector(Create_Recipe):
    def __init__(self, ingredient_menu_list, recipe_status):
        Create_Recipe.__init__(self)
        self.title = "Select Ingredients"
        self.info = "Many desktop publishing packages and web page editors now use Lorem Ipsum as " \
                    "their default model text"
        self.menu = ingredient_menu_list
        self.recipe_status = recipe_status

    def render_screen(self):
        self.refresh_screen()
        self.display_logo()
        self.display_info()
        self.display_recipe_status()
        self.display_menu()


class SaveRecipe(Create_Recipe):
    def __init__(self, recipe_to_save):
        Create_Recipe.__init__(self)
        self.title = "Save Recipe"
        self.info = ""
        self.recipe_to_save = recipe_to_save

    def render_screen(self):
        self.refresh_screen()
        self.display_logo()
        self.display_info()
        self.display_recipe_info()

    def display_recipe_info(self):
        info_text = f"\nRecipe has been created:\n" \
                    f"Name          >>>  {self.recipe_to_save.get_name}\n" \
                    f"Ingredients   >>>  {self.recipe_to_save.get_ingredients}"
        print(info_text)

    @staticmethod
    def display_saving_status():
        text = termcolor.colored(text="Data is being saved...", color="green")
        print(text)
        time.sleep(2)
        confirmation = termcolor.colored(text="Data saved successfully.", color="green")
        print(confirmation)
        time.sleep(2)


class AddIngredient(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.title = "Add ingredients"
        self.info = "All the Lorem Ipsum generators on the Internet tend to repeat predefined " \
                    "chunks as necessary"


class AddToComponent(ComponentSelector):
    def __init__(self, component_menu_list):
        ComponentSelector.__init__(self, components_menu_list=component_menu_list, recipe_status=None)
        self.info = "The standard chunk of Lorem Ipsum used since the 1500s is reproduced " \
                    "below for those interested."


class NewIngredient(AddIngredient):
    def __init__(self):
        AddIngredient.__init__(self)
        self.title = "Create New ingredient"
        self.info = "All the Lorem Ipsum generators on the Internet tend to repeat predefined " \
                    "chunks as necessary"


class SaveIngredient(NewIngredient):
    def __init__(self, new_value: str, values: list):
        NewIngredient.__init__(self)
        self.title = "Save ingredient"
        self.info = str()
        self.updated_values = values
        self.new_value = new_value

    def display_values(self):

        for value in self.updated_values:
            highlight = value
            if highlight == self.new_value:
                highlight = termcolor.colored(text=value, color='green')
            print(highlight)

    def render_screen(self):
        self.refresh_screen()
        self.display_logo()
        self.display_info()
        self.display_values()



def display_error(e):
    error = termcolor.colored(text=e.args[0], color='red')
    print(error)