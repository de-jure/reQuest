import json


def get_user_info():
    with open('savefile.json', 'r') as save_file:
        data = json.loads(save_file.read())

        return {
            'name': data['name'],
            'eurodollars': data['eurodollars'],
        }
