import requests, random

from fastapi import FastAPI, Request

app = FastAPI()

data = requests.get("http://135.181.118.171:7070/items/0").json()

@app.get("/")
def read_root(request: Request):
    print(request.headers)
    random_number = random.randint(0, len(data))
    return data[random_number]['item_key']

@app.get("/evt")
def read_root(request: Request):
    print(request.headers)
    return {"Thanks": "Bes"}