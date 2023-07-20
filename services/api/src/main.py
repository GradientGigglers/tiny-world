import requests, logging
from fastapi import FastAPI, Request, Depends
from .db import Session, get_db
from .models import RandomNumber

app = FastAPI()

@app.get("/")
def get_item(request: Request):
    user = request.headers.get('user')
    session = request.headers.get('session')
    print('Get /', 'user: ' + str(user), 'session: ' + str(session))

    return "f822c60d-6257-4c53-b448-0546d47ae877"


@app.post("/evt")
async def post_event(request: Request):
    #with open('../../static/evt.txt', 'w') as f:
        #print(request.headers, file=f)
    print(request.headers)
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
