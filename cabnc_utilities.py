import traceback
import json


def load_json_data(path, file_name):
    try:
        with open(path + file_name + ".json") as file:
            data = json.load(file)

    except (IOError, ValueError):
        traceback.print_exc()
        return False

    return data


def save_json_data(path, file_name, data):
    with open(path + file_name + '.json', 'w+') as file:
        json.dump(data, file, sort_keys=False, indent=4, separators=(',', ': '))


def load_text_data(path, verbose=True):
    with open(path, "r", encoding="utf8") as file:
        # Read a line and strip newline char
        lines = [line.rstrip('\r\n') for line in file.readlines()]
    if verbose:
        print("Loaded data from file %s." % path)
    return lines
