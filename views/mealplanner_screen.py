import views.screen


class MealplannerScreen(views.screen.Screen):

    def __init__(self, recipes_list: list):
        views.screen.Screen.__init__(self)
        self.title = "Mealplanner"
        self.menu_options = recipes_list
        self.info = ""

    def render_screen(self):
        self.display_title()
        self.display_info()
        self.display_menu()