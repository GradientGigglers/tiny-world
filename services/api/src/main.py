import requests, random

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(request: Request):

    print(request.headers)
    data = requests.get("http://135.181.118.171:7070/items/0").json()
    random_number = random.randint(0, len(data))
    return data[random_number]['item_key']

@app.get("/evt")
def read_root(request: Request):
    print(request.headers)
    return {"Thanks": "Bes"}