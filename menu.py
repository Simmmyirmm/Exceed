from pymongo import MongoClient
from fastapi import FastAPI
from fastapi import HTTPException
from typing import Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()

myClient = MongoClient('mongodb://localhost', 27017)

db = myClient["simdatabase"]
myCol = db["menu2"]

class Menu(BaseModel):
    name: str
    price: int
    amount: int

@app.post("/new-menu/")
def add_menu(m: Menu):
    x = jsonable_encoder(m)
    myCol.insert_one(x)
    return {
        "result": "done"
    }

@app.get("/menu/{name}")
def get_menu(name: str):
    result = myCol.find_one({"name": name}, {"_id": 0})
    print(result)
    if result != None:
        return {
            "result": result
        }
    else:
       raise HTTPException(404, f"Couldn't find menu with name: {name}'")


