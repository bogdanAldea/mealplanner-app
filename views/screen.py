"""
MODULE DEFINES VIEWS
"""
import pyfiglet
import termcolor
import textwrap
import os


class Screen:

    def __init__(self):
        self.title = None
        self.info = None
        self.menu_options = None

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()
        self.display_menu()

    @staticmethod
    def display_error(exception: Exception):
        error_text = termcolor.colored(text=exception.args[0], color="red")
        print(error_text)

    def display_info(self):
        wrapper_text = textwrap.fill(text=self.info, width=60)
        info_text = termcolor.colored(text=wrapper_text, color="cyan")
        print(info_text + "\n")

    def display_title(self):
        title_text = pyfiglet.figlet_format(text=self.title)
        print(title_text)

    def display_menu(self):
        for index, option in enumerate(self.menu_options):
            print(f"[{index+1}] {option}")

    @staticmethod
    def refresh_screen():
        os.system("cls")

    @staticmethod
    def display_update(update_message: str):
        message = termcolor.colored(text=update_message, color="green")
        print(message)