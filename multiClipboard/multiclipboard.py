import sys
import clipboard
import json


saved_data = 'clipboard.json'


def save_data(filepath, data):
    # pass data in the following format: (filepath and name, {"key": "value"})
    with open(filepath, 'w') as file:
        json.dump(data, file)


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(saved_data)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print('Data saved.')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print(f'"{key}" does not exist.')
    elif command == 'list':
        print(data)
    else:
        print('Unknown command')
else:
    print('Please pass exactly one command of the following: save, load, list')
