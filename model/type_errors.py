"""
Module for validating int and string values
"""


def request_type_int(prompt_message: str, error_message: str) -> int:
    """
    FUNCTION ASKS FOR USER INPUT WHICH MUST RETURN AN INT
    :param prompt_message: CONSOLE MESSAGE
    :param error_message: CONSOLE ERROR MESSAGE
    :return: int
    """
    # start infinite loop
    while True:
        # ask for input / if input is not a digit, catch the error and keep going
        try:
            raw_input = int(prompt_message)
            return raw_input
        except ValueError:
            print(error_message)
            continue


def request_type_alpha(prompt_message: str, error_message: str) -> str:
    """
    FUNCTION ASKS FOR USER INPUT WHICH MUST RETURN A STRING
    :param prompt_message:
    :param error_message:
    :return: string
    """
    # start infinite loop
    while True:
        # ask for user input
        raw_input = input(prompt_message)

        # verified string must allow space characters so in order to verify if all strings are alpha,
        # the input is split
        split_input = raw_input.split(sep=' ')

        """ passing the newly formed list to a function that iterates over list and
        checks if all strings are alpha"""
        string_integrity = check_alpha_integrity(LIST=split_input)
        if string_integrity is False:
            print(error_message)
            continue
        else:
            return " ".join(split_input)


def check_alpha_integrity(LIST: list) -> bool:
    for string in LIST:
        if string.isalpha() is True:
            continue
        else:
            return False