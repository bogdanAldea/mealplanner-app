"""
Main view module
"""


class View:

    @staticmethod
    def show_items_menu(list_items: list, title: str):
        print(20 * "+")
        print(title.upper())
        print(20 * "+")
        for item_index in range(1, len(list_items)+1):
            print(f"[{item_index}] {list_items[item_index-1]}")
        print(20 * "+")
