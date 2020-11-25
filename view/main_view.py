"""
Main view module
"""


class View:

    @staticmethod
    def show_items_menu(list_items: list, title: str, display_bullet_points=False):
        print(20 * "+")
        print(title.upper())
        print(20 * "+")
        for item_index in range(1, len(list_items)+1):
            if display_bullet_points is True:
                print("{bullet} {item}".format(bullet="*", item=list_items[item_index-1]))
            else:
                print("[{index}] {item}".format(index=item_index, item=list_items[item_index-1]))
        print(20 * "+")

    @staticmethod
    def read_stock_data(stock_data_list: dict):

        for main_key, main_value in stock_data_list.items():
            print("\n" + 20 * "+")
            print(main_key.upper())
            for sub_key, sub_value in main_value.items():
                print(sub_key + " -> " + str(sub_value))
