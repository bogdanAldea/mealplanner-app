"""
"""
import views.screen_manager as screen_manager


class NewIngredient(screen_manager.ScreenManager):

    def __init__(self):
        screen_manager.ScreenManager.__init__(self)
        self.title = "Create new ingredient"
        self.info_panel = "All the Lorem Ipsum generators on the Internet tend to repeat predefined " \
                          "chunks as necessary"