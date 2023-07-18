from fastapi import FastAPI, Request
from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import random 

engine = create_engine('postgresql://postgres:postgres@postgresql/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class RandomNumber(Base):
    __tablename__ = 'random_number'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    print(request.headers)
    return {"Hello": "From TinyWorld Again Again"}

@app.get("/evt")
def read_root(request: Request):
    print(request.headers)
    return {"Thanks": "Bes"}

@app.get("/get-random-number")
async def get_random_number():
    number = session.query(RandomNumber).filter_by(id=1).first()
    return {"number": number.number}

@app.get("/set-random-number")
async def set_random_number():
    existing_number = session.query(RandomNumber).filter_by(id=1).first()
    if existing_number:
        session.delete(existing_number)
        session.commit()
    number = RandomNumber(id=1, number=random.randint(1, 100)) 
    session.add(number)
    session.commit()
    session.close()   