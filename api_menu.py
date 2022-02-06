from pymongo import MongoClient
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

client = MongoClient('mongodb://localhost', 27017)
db = client["Project1"]
menu_collection = db["User"]

@app.get("/fruit/all")
def get_all_fruit():
    r = menu_collection.find({}, {"_id": 0, "name": 1})
    my_result = {}
    count = 1
    for i in r:
        my_result[count] = i
        count += 1
    return {
        "result": my_result
    }

@app.post("/fruit/add/{name}/{price}")
def add_new_fruit(name: str, price: int):
    new_fruit = {
        "name": name,
        "price": price
    }
    menu_collection.insert_one(new_fruit)
    return {
        "result": "done"
    }

@app.delete("/fruit/delete/{name}")
def remove_one_fruit(name: str):
    query = {"name": name}
    menu_collection.delete_one(query)
    return {
        "result": "done"
    }

@app.put("/fruit/update/{name}/{new_price}")
def update_price(name: str,new_price: int):
    query = {"name": name}
    new_values = {"$set": {"price": new_price}}
    menu_collection.update_many(query, new_values)
    return {
        "result": "done"
    }