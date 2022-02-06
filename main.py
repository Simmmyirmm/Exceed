# from fastapi import FastAPI
# from typing import Optional

# app = FastAPI()

# students = {
#     "5751": {
#         "name": "Best",
#         "age": 19
#     },
#     "1234": {
#         "name": "Boom",
#         "age": 20
#     }
# }

# @app.get("/find/students")
# def info_all_student():
#     return {
#         "student": students
#     }

# @app.get("/find/students/{student_id}/")
# def find_info_std(student_id):
#     return {
#         "info": students[student_id]
#     }

# @app.get("/find/students/{student_id}/name")
# def find_name_std(student_id):
#     return {
#         "name": students[student_id]["name"]
#     }

# @app.get("/find/students/{student_id}/age")
# def find_age_std(student_id):
#     return {
#         "age": students[student_id]["age"]
#     }

# @app.post("/add/students/{student_id}")
# def add_info(student_id: str, name: Optional[str] = None,
# age: Optional[int] = None):
#     students[student_id] = {
#         "name": name,
#         "age": age
#     }
#     return {
#         "add student complete!!!"
#     }


# use basemodel
# input by body
# {
#     "id": "ENTER_ID",
#     "name": "ENTER_NAME",
#     "age": Optional

# }
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    "5751": {
        "name": "Besto",
        "age": 19
    },
     "5769": {
        "name": "MC",
        "age": 20
    }
}

class student(BaseModel):
    id: str
    name: str
    age: Optional[int] = None

@app.post("/add/")
def add_student(std: student):
    students[std.id] = std
    return "add complete!!!"

@app.get("/find/all/")
def find_all_student():
    return students

@app.get("/find/student/")
def find_student(id: Optional[str]):
    return {
        "info": students[id]
    }
