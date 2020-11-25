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
            user_request = request_type_alpha(prompt_message="\nModifica {item} [da/nu] >> ".format(item=category),
                                              error_message="Eroare input: optiunea trebuie sa fie formata doar din litere.")
            if user_request in accept_selector:
                print("Modificare {} selectata".format(category).upper())
                for ingredient, quantity in ingredient_data.items():
                    while True:
                        # ASK USER IF WANTS O UPDATED THIS SUB-ITEM'S QUANTITY
                        user_ingredient_option = request_type_alpha(prompt_message="Modifica {sub_item} [da/nu] >> ".format(sub_item=ingredient),
                                                                    error_message="Eroare input: optiunea trebuie sa fie formata doar din litere.")
                        if user_ingredient_option in accept_selector:
                            new_quantity = request_type_int(prompt_message="Cantitate/Gramaj {} >> ".format(ingredient),
                                                            error_message="Eroare input: cantitatea trebuie sa fie formata doar din cifre.")
                            ingredient_data[ingredient] = new_quantity
                            print(colored("Cantitatea pentru {INGREDIENT}  a fost schimbata din {OLD} in {NEW}".format(INGREDIENT=ingredient, OLD=quantity, NEW=new_quantity), "green"))
                        elif user_ingredient_option in reject_selector:
                            break
                        else:
                            print(colored("Optiunele valide sunt da sau nu.", "red"))
                            continue
                        break
                    continue
                break
            elif user_request in reject_selector:
                break
            else:
                print(colored("Optiunile valide sunt da sau nu.", "red"))
                continue

    return stocks_json_data


                # IF ITEM IS SELECTED -> PRINT INGREDIENT AND CHANGE VALUE
    #             for ingredient, quantity in ingredient_data.items():
    #                 new_quantity = request_type_int(prompt_message="Cantitate/Gramaj {} >> ".format(ingredient),
    #                                                 error_message="Eroare input: cantitatea trebuie sa fie formata doar din cifre.")
    #                 ingredient_data[ingredient] = new_quantity
    #                 print("==== Cantitatea pentru {INGREDIENT}  a fost schimbata din {OLD} in {NEW} ===="
    #                       .format(INGREDIENT=ingredient, OLD=quantity, NEW=new_quantity))
    #         elif user_request in reject_selector:
    #             break
    #         else:
    #             continue
    #         break
    # return stocks_json_data
