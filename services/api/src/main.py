from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    print(request.headers)
    return {"Hello": "From TinyWorld Again"}