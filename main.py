from fastapi import FastAPI

from src.saves import create_savefile
from src.user import get_user_info
from src.jobs import work1


create_savefile()
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello, unknown!'}

@app.get('/me')
async def me():
    return get_user_info()

@app.get('/work')
async def work():
    return work1()
