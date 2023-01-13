from datetime import datetime
import json

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    dictionary = {
        'name': 'dejure',
        'createdAt': datetime.now().timestamp(),
        'eurodollars': 0,
        'items': [],
        'implants': [],
        'timestamps': {
            'last_worktime': 0,
        },
    }

    with open('savefile.json', 'w') as save_file:
        save_file.write(json.dumps(dictionary, indent=2))

    return {
        'message': 'Hello dejure',
    }

@app.get('/me')
async def me():
    with open('savefile.json', 'r') as save_file:
        data = json.loads(save_file.read())

        return {
            'name': data['name'],
            'eurodollars': data['eurodollars'],
        }

@app.get('/work')
async def work():
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
