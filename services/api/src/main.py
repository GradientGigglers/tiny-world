import requests, logging
from fastapi import FastAPI, Request, Depends
from .db import Session, get_db
from .models import RandomNumber
import random
import open

app = FastAPI()

data = [{"item_key": "item_value"}, {"item_key": "item_value"}]


response = requests.get("http://135.181.118.171:7070/items/0")
if response.status_code != 200:
    print("Non-200 response code: " + str(response.status_code))
else:
    data = response.json()


@app.get("/")
def get_item(request: Request):
    user = request.headers.get('user')
    session = request.headers.get('session')
    print('Get /', 'user: ' + str(user), 'session: ' + str(session))

    random_number = random.randint(0, len(data) - 1)
    return data[random_number]['item_key']


@app.post("/evt")
async def post_event(request: Request):
    with open('evt.txt', 'w') as f:
        print(request.headers, file=f)
    return {"Thanks": "Bes"}

@app.get("/get-random-number")
async def get_random_number(db: Session = Depends(get_db)):
    number = db.query(RandomNumber).filter_by(id=1).first()
    return {"number": number.number}


@app.get("/set-random-number")
async def set_random_number(db: Session = Depends(get_db)):
    existing_number = db.query(RandomNumber).filter_by(id=1).first()
    if existing_number:
        db.delete(existing_number)
        db.commit()
    number = RandomNumber(id=1, number=random.randint(1, 5))
    db.add(number)
    db.commit()
    db.close()
