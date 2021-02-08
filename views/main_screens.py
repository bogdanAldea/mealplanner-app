"""
"""
import views.screen_manager as screen_manager


class CreateRecipeScreen(screen_manager.ScreenManager):

    def __init__(self):
        screen_manager.ScreenManager.__init__(self)
        self.title = "Create new recipe"
        self.info_panel = "There are many variations of passages of Lorem Ipsum available, but the " \
                          "majority have suffered alteration in some form, by injected humour"

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
