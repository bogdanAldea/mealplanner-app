from mealplanner_app.model.json_backend import data_is_stored
from mealplanner_app.model.type_errors import *

"""
FUNCTION FOR EDIT MENU
    -   add new recipe
    -   edit a component
    -   add a new category
"""


# FUNCTION ALLOWS FOR NEW RECIPE CREATIONS
def create_new_recipe(recipe_components: dict, loaded_json_data: dict) -> dict:
    """

    :param recipe_components: elements for building new recipes
    :param loaded_json_data: existing data with all stored recipes
    :return: export_new_recipe -> dict
    """
    export_new_recipe = dict()
    this_recipe_ingredients = dict()

    # SET RECIPE NAME TO USE AS DICT KEY AND CHECK IF ALREADY EXISTS OR NOT
    RECIPE_NAME = str()
    while True:
        temp_name = request_type_alpha(prompt_message="Nume reteta noua >> ",
                                       error_message="Eroare input: numele trebuie sa fie format doar din litere")

        # CHECK IF THIS NAME ALREADY EXISTS OR NOT
        if data_is_stored(new_data=temp_name, current_loaded_data=loaded_json_data) is True:
            continue
        else:
            RECIPE_NAME += temp_name
            break

    # SET INGREDIENTS AND QUANTITIES FORM COMPONENTS
    for ingredient_category, ingredient_list in recipe_components.items():
        while True:
            # USER IS ASKED IF WANTS TO ADD A SPECIFIC CATEGORY
            add_category = request_type_alpha(prompt_message="Adauga {}?[da/nu] >> ".format(ingredient_category),
                                              error_message="Eroare input: optiunea trebuie sa fie formata doar din litere.")
            if add_category == 'da' or add_category == 'da'.capitalize() or add_category == 'da'.upper():
                # IF CATEGORY IS SELECTED -> PRINT EACH INGREDIENT AND ASK FOR QUANTITY
                for ingredient in ingredient_list:
                    quantity = request_type_int(prompt_message="Cantitate/Gramaj {} >> ".format(ingredient),
                                                error_message="Eroare input: cantitatea trebuie sa fie formata doar din cifre.")
                    # ADD ONLY QUANTITIES THAT ARE GREATER THAN 0
                    if quantity > 0:
                        this_recipe_ingredients[ingredient] = quantity

            elif add_category == "nu" or add_category == "nu".capitalize() or add_category == "nu".upper():
                # IF CATEGORY IS NOT SELECTED, JUMP TO THE NEXT ONE
                break
            else:
                print("Eroare input: optiunile valide sunt Da / Nu.")
                continue
            break

    export_new_recipe[RECIPE_NAME] = this_recipe_ingredients
    return export_new_recipe


# FUNCTION THAT CREATED A NEW CATEGORY INSIDE COMPONENTS WITH NEW LIST OF UNIQUE INGREDIENTS AS VALUES
def edit_components(components_data: dict) -> tuple:
    """
    FUNCTION CREATES A NEW CATEGORY AND ADDS IT TO BOTH COMPONENTS AND STOCKS
    IN COMPONENTS IS ADDED A NEW COMPONENT DICT WITH A UNIQUE NEW NAME AND A LIST OF INGREDIENTS
    IN STOCK IS ADDED A NEW COMPONENTS DICT WITH THE SAME UNIQUE NAME AND A DICT WITH INGREDIENT NAME AS KEYS AND 0 AS VALUES
    :param components_data:
    :return:
    """
    NEW_CATEGORY_NAME = str()  # -> key of dict
    COMPONENTS_INGREDIENTS_LIST = list()
    STOCKS_INGREDIENTS_LIST = dict()
    NEW_COMPONENT_IN_COMPONENTS = dict()
    NEW_COMPONENT_IN_STOCKS = dict()

    # SET NAME FOR THE NEW COMPONENT
    while True:
        category_name = request_type_alpha(prompt_message="Nume categorie noua >> ",
                                           error_message="Eroare input: numele categoriei trebuie sa fie format doar din litere.")

        # CHECK IF THIS NEW COMPONENTS EXISTS ALREADY OR NOT
        if data_is_stored(new_data=category_name, current_loaded_data=components_data):
            continue
        else:
            NEW_CATEGORY_NAME = category_name
            break

    # START ADDING DESIRED INGREDIENTS THROUGH INPUT
    while True:
        loop_stop_flag = ["STOP", 'stop', "Stop"]
        ingredient_name = request_type_alpha(prompt_message="Ingredient nou >> ",
                                             error_message="Eroare input: numele ingredientului trebuie sa fie format doar din litere.")
        if ingredient_name not in loop_stop_flag:
            if ingredient_name not in COMPONENTS_INGREDIENTS_LIST and ingredient_name not in STOCKS_INGREDIENTS_LIST.keys():
                COMPONENTS_INGREDIENTS_LIST.append(ingredient_name)
                STOCKS_INGREDIENTS_LIST[ingredient_name] = 0
        elif ingredient_name in loop_stop_flag:
            break
        else:
            print("Pentru a opri adaugarea, tasteaza 'stop'.")
            continue

    NEW_COMPONENT_IN_COMPONENTS[NEW_CATEGORY_NAME] = COMPONENTS_INGREDIENTS_LIST
    NEW_COMPONENT_IN_STOCKS[NEW_CATEGORY_NAME] = STOCKS_INGREDIENTS_LIST
    return NEW_COMPONENT_IN_COMPONENTS, NEW_COMPONENT_IN_STOCKS


# FUNCTION THAT ADDS A NEW UNIQUE INGREDIENT TO EXISTING CATEGORY
def add_new_ingredient(components_data: dict, stocks_data: dict, menu_listing: list):
    """
    FUNCTION ADD THE NEW INGREDIENT TO BOTH THE COMPONENTS AND STOCK DATA
    :param components_data: ingredient is added here
    :param stocks_data:
    :param menu_listing: menu display to select component to which the ingredient is added
    :return: components dict, and stocks dict as tuple for updating files
    """
    # START INFINITE LOOP
    while True:
        # ASK USER TO SELECT OPTION FROM MENU TO UPDATE WITH NEW ITEMS
        menu_selector = request_type_int(prompt_message="Alege categoria >> ",
                                         error_message="Eroare input selectie: introdu doar cifre.")

        # CHECK IF USER'S OPTION EXISTS IN THE RANGE OF THE MENU
        if menu_selector in range(1, len(menu_listing)+1):

            # IF EXISTS -> GET THE OPTION
            for menu_item_index in range(1, len(menu_listing)+1):
                if menu_selector == menu_item_index:

                    # TARGET OPTION IN COMPONENTS DATA
                    for components_name, components_list in components_data.items():
                        for stock_name, stock_list in stocks_data.items():

                            # WHEN TARGET IS REACHED, ASK USER FOR NEW INGREDIENT
                            if menu_listing[menu_item_index-1] == components_name and menu_listing[menu_item_index-1] == stock_name:

                                # START ADDING INGREDIENTS IN INFINITE LOOP
                                while True:
                                    loop_stop_flag = ["stop", "Stop", "STOP"]
                                    new_ingredient = request_type_alpha(prompt_message="Ingredient nou >> ",
                                                                        error_message="Eroare input: numele ingredientului trebuie sa fie format doar din litere.")

                                    if new_ingredient not in loop_stop_flag:
                                        if new_ingredient not in components_list and new_ingredient not in stock_list:
                                            components_list.append(new_ingredient)
                                            stock_list[new_ingredient] = 0
                                        else:
                                            print("{} stocat deja".format(new_ingredient))
                                            continue

                                    elif new_ingredient in loop_stop_flag:
                                        break
                                    else:
                                        print("Pentru a opri adaugarea, introdu 'stop'.")
                                        continue
                else:
                    continue
        else:
            print("Eroare selectie: alege numarul specific din meniul afisat.")
            continue
        return components_data, stocks_data


