"""

"""
from pyfiglet import figlet_format
import platform
import termcolor
import textwrap
import os
import time


class ScreenManager:

    def __init__(self):
        self.title = str()
        self.info_panel = str()
        self.menu_options = list()

    def render_screen(self):
        self.refresh_screen()
        self.display_title()
        self.display_info()

    @staticmethod
    def refresh_screen():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def display_error_message(exception_error: Exception) -> None:
        error_text = termcolor.colored(text=exception_error.args[0], color='red')
        print(error_text)

    def display_info(self):
        info_text = textwrap.fill(text=self.info_panel, width=60)
        info_text = termcolor.colored(text=info_text, color='cyan')
        print(info_text+"\n")

    def display_title(self):
        screen_title = figlet_format(text=self.title)
        print(screen_title)

    def display_menu(self):
        for index, item in enumerate(self.menu_options):
            menu_line = f"[{index+1}] {item}"
            print(menu_line)
