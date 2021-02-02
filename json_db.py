import json


def read_file(file_path):
    with open(file=file_path, mode='r') as file:
        return file.read()


def load_data(file_data):
    return json.loads(file_data)


def save_data(new_data, file):
    with open(file, 'w') as file:
        json.dump(new_data, file, indent=4)