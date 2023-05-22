import json


def json_file_to_dict(_file):
    with open(_file) as config_file:
        config = json.load(config_file)
        return config
    
config = json_file_to_dict("./config.json")

def convert_unicode_to_dict(data):
    result = {}
    data = dict(data)
    print(data)
    for field, value in data.items():
        result[field.encode('ascii', 'ignore')] = value.encode('ascii', 'ignore')
    return result
