import json


def read_file(file_path):
    with open(file=file_path, mode='r') as file:
        return file.read()


def load_data(file_data):
    return json.loads(file_data)


def save_data(new_data):
    return json.dumps(new_data)


def update_file(file_path, new_data):
    with open(file=file_path, mode='w') as file:
        file.write(new_data)