from datetime import datetime
import json
import os


def create_savefile():
    if not os.path.exists('savefile.json'):
        with open('savefile.json', 'w') as save_file:
            save_file.write(json.dumps({
                'name': 'unknown',
                'createdAt': datetime.now().timestamp(),
                'eurodollars': 0,
                'items': [],
                'implants': [],
                'timestamps': {
                    'last_worktime': 0,
                },
            }, indent=2))

def delete_savefile():
    if os.path.exists('savefile.json'):
        os.remove('savefile.json')
