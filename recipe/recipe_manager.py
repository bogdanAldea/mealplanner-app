"""
"""
import mealplanner_app.json_db as json_db


class RecipeManager:

    def __init__(self, database_path):
        self.database = database_path
        self.connection: list = self.read_database_file()
        self.loaded_data: list = self.load()

    def read_database_file(self) -> list:
        return json_db.read_file(file_path=self.database)

    def save(self, data_to_save) -> list:
        saved_data = json_db.save_data(new_data=data_to_save)
        self.loaded_data.append(saved_data)
        return self.loaded_data

    def load(self) -> list:
        loaded_data = json_db.load_data(file_data=self.connection)
        return loaded_data