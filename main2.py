from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {}

class student(BaseModel):
    id: str
    name: str
    age: Optional[int] = None

@app.post("/add/")
def add_student(std: student):
    students[std.id] = std
    return "add complete!!!"