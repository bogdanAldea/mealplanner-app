import os

"""
Module for handling all components for the mealplanner functionality
"""


def get_user_option(available_recipes_list: list):
    """

    :param available_recipes_list:
    :return:
    """
    user_options_selection = list()
    loop_stop_flag = ['stop', 'Stop', 'STOP']
    while True:
        user_request = input("Alege o reteta >> ")
        if user_request.isdigit() is True:
            user_request = int(user_request)
            if user_request in range(1, len(available_recipes_list)+1):
                user_options_selection.append(available_recipes_list[user_request-1])
        elif user_request in loop_stop_flag:
            return user_options_selection
        else:
            continue


def get_preliminary_list(recipe_json_data: dict, selected_recipes: list) -> dict:
    """

    :param recipe_json_data:
    :param selected_recipes:
    :return:
    """
    preliminary_shopping_list = dict()
    for recipe in selected_recipes:
        for recipe_name, recipe_components in recipe_json_data.items():
            if recipe == recipe_name:
                for ingredient, quantity in recipe_components.items():
                    if ingredient not in preliminary_shopping_list.keys():
                        preliminary_shopping_list[ingredient] = quantity
                    else:
                        preliminary_shopping_list[ingredient] += quantity
    return preliminary_shopping_list


def get_shopping_list(preliminary_list: dict, stock_json_data: dict) -> tuple:
    """

    :param preliminary_list:
    :param stock_json_data:
    :return:
    """
    export_shopping_list = dict()
    for category_name_in_stocks, components_in_stocks in stock_json_data.items():
        for item_to_buy, item_quantity_to_buy in preliminary_list.items():
            for stock_item, stock_item_quantity in components_in_stocks.items():
                if item_to_buy == stock_item:
                    if stock_item_quantity < item_quantity_to_buy:
                        new_quantity = abs(stock_item_quantity - item_quantity_to_buy)
                        export_shopping_list[category_name_in_stocks] = {item_to_buy: new_quantity}
                        components_in_stocks[stock_item] = 0
    return export_shopping_list, stock_json_data


def start_mealplanner(available_options: list, recipe_data: dict, stock_data: dict) -> tuple:
    options_request = get_user_option(available_recipes_list=available_options)
    pre_shop_list = get_preliminary_list(recipe_json_data=recipe_data, selected_recipes=options_request)
    shopping_cart, updated_stocks = get_shopping_list(preliminary_list=pre_shop_list, stock_json_data=stock_data)
    return shopping_cart, updated_stocks


def write_cart_list_to_file(CART_LIST: dict):
    separator = 20 * "="
    filename = "mealplan"
    shopping_cart_index = 0
    while True:
        file_path = filename + str(shopping_cart_index) + ".txt"
        if os.path.isfile(file_path) is True:
            shopping_cart_index += 1
            continue
        else:
            file = open(file_path, "w")
            for category_name, components in CART_LIST.items():
                file.write(separator + "\n")
                file.write(category_name.upper() + "\n")
                for ingredient, quantity in components.items():
                    file.write(ingredient + ": " + str(quantity) + "\n")
            file.close()
            break
