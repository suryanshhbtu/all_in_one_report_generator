from pydantic import BaseModel
from typing import List

class Parent(BaseModel):
    fatherName: str
    motherName: str

class Subject(BaseModel):
    name: str
    marks: int

class Student(BaseModel):
    id: int
    name: str
    age: int
    parents: Parent
    subjects: List[Subject]
