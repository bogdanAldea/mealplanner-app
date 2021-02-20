"""
MODULE DEFINES THE PARENT CLASS MODEL
"""
import models.exceptions
import settings


class Model:
    """
    Class represents the model parent class that will handle business logic shared by
    child classes.
    """

    # exceptions module
    exceptions = models.exceptions

    def __init__(self):
        """
        Constructor of parent model class.
        """

        # define the database file that each child will use to update its data.
        self.database_file = None

        # define dictionary of existing components
        self.installed_components = settings.INSTALLED

    @classmethod
    def validate_menu_request(cls, request, options_list) -> int:
        """
        Method takes the request from user and checks if exists inside given list of options.
        :param request: int
        :param options_list: list
        :return: int
        """

        # check if user's request exists in given list of options
        if request in range(1, len(options_list)+1):
            return request

        else:
            # if request is invalid / outside the size of given list, raise exception
            raise cls.exceptions.MenuOptionInvalid("Your input for a menu option si invalid.")

    @classmethod
    def validate_recipe_name(cls, name_to_validate: str, stored_recipe_name: list) -> str:
        """
        Method takes user's request for a new recipe name and checks if it already exists
        in a list of already stored names.

        :param name_to_validate: str
        :param stored_recipe_name: list
        :return: str
        """
        if name_to_validate not in stored_recipe_name:
            return name_to_validate
        else:
            raise cls.exceptions.RecipeIsStored(f"Recipe with the name <{name_to_validate}> is already stored.")

    @classmethod
    def validate_save_request(cls, user_request) -> str:
        """
        Method checks if user's request matches the values for save request.
        :param user_request: str
        :return: str
        """
        if user_request in ["y", "Y"] or user_request in ["n", "N"]:
            return user_request
        else:
            raise cls.exceptions.InvalidSaveRequest("Option invalid. The only valid option are [y, Y] for Yes and [n, N] for No.")
