from datetime import datetime
import json


def work1():
    with open('savefile.json', 'r+') as save_file:
        data = json.load(save_file)
        if data['timestamps']['last_worktime'] + 10 < datetime.now().timestamp():
            data['eurodollars'] += 10
            data['timestamps']['last_worktime'] = datetime.now().timestamp()
            save_file.seek(0)
            json.dump(data, save_file, indent=2)
            save_file.truncate()

            return {
                'message': 'Earned 10 ED',
            }
        return {
            'message': 'You can\'t work that often. Try again later.',
        }
