import json

def read_json_file(file_path=""):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

status = read_json_file("json/status.json")
dbinfo = read_json_file("json/info.json")