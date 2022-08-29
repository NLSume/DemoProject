from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/")
async def root():
    return {'message': 'Hello World'}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return{"item_id" : item_id}