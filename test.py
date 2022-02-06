from unittest import result
from fastapi import Query
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client["simdatabase"]
Collections = db["menu"]

mylist = client.list_database_names()

print(mylist)

orange = {
    "name": "Orange",
    "price": 40,
    "amount": 100
}

apple = {
    "name": "apple",
    "price": 100
}

banana = {
    "name": "Banana",
    "price": 20
}

Collections.insert_one(orange)

fruit_list = []
fruit_list.append(apple)
fruit_list.append(banana)

x = Collections.insert_many(fruit_list)
print(x.inserted_ids)

y = Collections.find({},{"_id": 0,"name": 1, "price": 1})
for i in y:
    print(i)

query = {"name": "Orange", "price": 300}
result = Collections.find(query, {"price": 1})
for i in result:
    print(i)

query = {"name": "Orange"}
result = Collections.find_one(query, {"_id": 0, "price": 1})
print(result)

query = {"price": {"$lt": 50}}
result = Collections.find(query)
for i in result:
    print(i)

query = {"name": "besto"}
result = Collections.delete_many(query)

query = {"name": "Banana"}
newvalues = {"$set" : {"name": "banana"}}
Collections.update_many(query, newvalues)

