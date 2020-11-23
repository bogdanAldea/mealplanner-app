import json
from json import JSONDecodeError

"""
Backend communication module with json files
    - creates data
    - reads data
    - updates data
"""


# OPEN JSON FILE AND READ ALL DATA AVAILABLE
def read_json_from_file(json_file) -> dict:
    """
    FUNCTION OPENS JSON FILE AND GETS ALL DATA
    :param json_file:  ".json" file
    :return: dict with all data
    """
    file = open(file=json_file, mode="r")
    file_data = file.read()
    try:
        json_data = json.loads(file_data)
        return json_data
    except JSONDecodeError:
        print("Fisierul {this_file} este gol".format(this_file=json_file))
    file.close()


# VERIFY IF LOADED DATA ALREADY EXISTS IN GIVEN JSON DATA
def data_is_stored(new_data: str, current_loaded_data: dict) -> bool:
    """
    FUNCTION CHECKS IF A NEW DATA IS STORED OR NOT IN CURRENT DATA BY COMPARING KEYS
    :param new_data: KEY OF DATA TO BE UPDATED
    :param current_loaded_data: DICT WITH CURRENT LOADED DATA
    :return: TRUE IF DATA IS STORED, FALSE F DATA IS NOT STORED
    """
    temp_current_keys = list()
    for current_data_keys in current_loaded_data.keys():
        temp_current_keys.append(current_data_keys)
    if new_data in temp_current_keys:
        print("{} already stored.".format(new_data))
        return True
    else:
        return False


# UPDATE JSON DATA WITH NEW DATA
def update_json_data(current_data: dict, new_data_to_store: dict) -> dict:
    """
    FUNCTION UPDATES CURRENT DATA DICT WITH NEW DATA IF NOT STORED ALREADY
    :param current_data: DICT OF CURRENT DATA LOADED IN SYSTEM
    :param new_data_to_store: MODIFIED OR NEWLY CREATED DATA TO UPDATE
    :return: updated current data
    """
    current_data.update(new_data_to_store)
    return current_data


# UPDATE JSON FILE WITH THE NEW UPDATED DATA
def update_json_file(filename, updated_jso_data: dict):
    """
    FUNCTION WRITES THE NEW JSON DATA TO EXISTING JSON FILE
    :param filename: SPECIFIC JSON FILE TO WRITE DATA TO
    :param updated_jso_data: UPDATED NEW DICT
    :return: NONE
    """
    file = open(file=filename, mode="w")
    json_data = json.dumps(updated_jso_data, indent=4)
    file.write(json_data)
    file.close()