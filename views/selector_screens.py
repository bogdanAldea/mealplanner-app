"""
"""
import views.screen_manager as screen_manager
import termcolor


class ComponentSelector(screen_manager.ScreenManager):

    def __init__(self, components_list: list, recipe_status):
        screen_manager.ScreenManager.__init__(self)
        self.title = "Select component"
        self.info_panel = "It is a long established fact that a reader will be distracted by " \
                          "the readable content of a page when looking at its layout."

        self.menu_options = components_list
        self.recipe_status = recipe_status

    def display_recipe_status(self):

        if self.recipe_status is not None:
            # unpack dictionary keys & values
            field_a, field_b = list(self.recipe_status.keys())
            content_a, content_b = list(self.recipe_status.values())

            # add color & formatting to keys
            field_a = termcolor.colored(text=field_a.upper(), color='green')
            field_b = termcolor.colored(text=field_b.upper(), color='green')

            # print status to the screen
            status = f"{field_a}: {content_b}\n{field_b}: {content_b}"
            print(status)

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
        if self.recipe_status is not None:
            self.display_recipe_status()
        else:
            pass
        self.display_menu()


class IngredientSelector(ComponentSelector):

    def __init__(self, ingredient_menu_list, recipe_status):
        ComponentSelector.__init__(self, components_list=ingredient_menu_list, recipe_status=recipe_status)
        self.title = "Select ingredient"
        self.info_panel = "Many desktop publishing packages and web page editors now use Lorem Ipsum as " \
                          "their default model text"
        self.menu_options = ingredient_menu_list
        self.recipe_status = recipe_status


class AddToComponent(ComponentSelector):

    def __init__(self, component_menu_list):
        ComponentSelector.__init__(self, components_list=component_menu_list, recipe_status=None)
        self.info_panel = "The standard chunk of Lorem Ipsum used since the 1500s is reproduced " \
                          "below for those interested."