"""
Function that reads items from given json data structure and returns a list og items
"""


def read_items(json_data, data_type_is_dict=True) -> list:
    """
    FUNCION THAT READ A GIVEN DATA STRUCTURE AND RETURN A LIST WITH ITEMS THAT HAVE BEEN READ
    :param json_data: if True -> data is a dict, else data is a list, tuple, set
    :param data_type_is_dict:
    :return:
    """
    temp_items_list = list()
    if data_type_is_dict:
        for item in json_data.keys():
            temp_items_list.append(item)
    else:
        for item in json_data:
            temp_items_list.append(item)
    return temp_items_list