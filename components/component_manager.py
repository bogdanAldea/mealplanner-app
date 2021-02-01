"""
"""
import json_db


class ComponentManager:

    def __init__(self, database_path, installed_components: dict):
        self.database = database_path
        self.installed_components: dict = installed_components
        self.connection: dict = self.read_database_file()
        self.loaded_data: dict = self.load()

    def read_database_file(self):
        return json_db.read_file(file_path=self.database)

    def save(self, data_to_save: dict) -> dict:
        new_data: dict = json_db.save_data(new_data=data_to_save)
        self.loaded_data.update(new_data)
        return self.loaded_data

    def load(self) -> dict:
        loaded_data: dict = json_db.load_data(file_data=self.connection)
        return loaded_data

    def update(self, data_to_update: dict) -> None:
        json_db.update_file(file_path=self.database, new_data=data_to_update)

    def select_component_values(self, request: int) -> list:
        installed_components: list = list(self.loaded_data.keys())
        target_component: str = installed_components[request-1]
        ingredients_value_list: list = self.loaded_data.get(target_component)
        return ingredients_value_list

    @staticmethod
    def select_from_values(request, values):
        return values[request-1]