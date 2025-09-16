from pydantic import BaseModel

# Define the Student model
class Student(BaseModel):
    id: int
    name: str
    age: int
