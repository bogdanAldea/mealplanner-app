from mealplanner_app.model.type_errors import *

"""
Backend module for updating stocks data file
"""


def update_stock_values(stocks_json_data: dict) -> dict:
    """

    :param stocks_json_data:
    :return:
    """
    # ITERATE OVER STOCK DICT KEYS AND VALUES
    for category, ingredient_data in stocks_json_data.items():
        accept_selector = ['da', 'Da', 'DA']
        reject_selector = ['nu', 'Nu', 'NU']
        while True:
            # ASK USER TO SELECT WHICH ITEM TI UPDATE
            user_request = request_type_alpha(prompt_message="Modifica {item} [da/nu] >> ".format(item=category),
                                              error_message="Eroare input: optiunea trebuie sa fie formata doar din litere.")
            if user_request in accept_selector:
                print("Modificare {}\n".format(ingredient))
                # IF ITEM IS SELECTED -> PRINT INGREDIENT AND CHANGE VALUE
                for ingredient, quantity in ingredient_data.items():
                    new_quantity = request_type_int(prompt_message="Cantitate/Gramaj {} >> ".format(ingredient),
                                                    error_message="Eroare input: cantitatea trebuie sa fie formata doar din cifre.")
                    ingredient_data[ingredient] = new_quantity
                    print("\nCantitatea pentru {INGREDIENT}  a fost schimbata din {OLD} in {NEW}\n"
                          .format(INGREDIENT=ingredient, OLD=quantity, NEW=new_quantity))
            elif user_request in reject_selector:
                break
            else:
                continue
            break
    return stocks_json_data
