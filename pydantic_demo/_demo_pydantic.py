from pydantic import BaseModel , EmailStr
from typing import Optional 

class Student(BaseModel):
    name: str = "nitish"
    age:Optional[int] = None
    email:EmailStr



new_student = {"age":14,"email":"abc"}
student = Student(**new_student)
print(student) 




