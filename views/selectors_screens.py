"""

"""
import views.screen
import termcolor


class ComponentSelectorScreen(views.screen.Screen):

    def __init__(self, components_list: list, recipe_status):
        views.screen.Screen.__init__(self)
        self.title = "Select component"
        self.info = "It is a long established fact that a reader will be distracted by " \
                    "the readable content of a page when looking at its layout."

        self.menu_options = components_list
        self.recipe_status = recipe_status

    def display_recipe_status(self):

        if self.recipe_status is not None:

            # unpack status dictionary keys & values
            name_field, items_field = list(self.recipe_status.keys())
            name_content, items_content = list(self.recipe_status.values())

            # add color & formatting to keys
            name_field: str = termcolor.colored(text=name_field.upper(), color="green")
            items_field: str = termcolor.colored(text=items_field.upper(), color="green")

            # print status to the screen
            status = f"{name_field}: {name_content}\n{items_field}: {items_content}"
            print(status)

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
        if self.recipe_status is not None:
            self.display_recipe_status()
        self.display_menu()


class IngredientSelectorScreen(ComponentSelectorScreen):

    def __init__(self, ingredients_list: list, recipe_status: dict):
        ComponentSelectorScreen.__init__(self, ingredients_list, recipe_status)
        self.title = "Select ingredient"
        self.info = "Many desktop publishing packages and web page editors now use Lorem Ipsum as " \
                          "their default model text"
        self.menu_options = ingredients_list
        self.recipe_status = recipe_status

# if __name__ == '__main__':
#     recipe_status = {"x": str(), "y": list()}
#     comp_list = ["option a", "option b", "option c", "option d"]
#     screen = ComponentSelectorScreen(comp_list, recipe_status)
#     screen.render_screen()