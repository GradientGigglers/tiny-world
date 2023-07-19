import requests, random
from fastapi import FastAPI, Request, Depends
from .db import Session, get_db
from .models import RandomNumber
import random 

app = FastAPI()

data = requests.get("http://135.181.118.171:7070/items/0").json()

@app.get("/")
def read_root(request: Request):
    print(request.headers)
    random_number = random.randint(0, len(data))
    return data[random_number]['item_key']

@app.post("/evt")
def read_root(request: Request):
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