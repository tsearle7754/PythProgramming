from pathlib import Path
import hashlib
from nicegui import ui

class Person:
    def __init__(self, name, id, email):
        self.__name = name
        self.__id = id
        self.__email = email
    
    def to_dict(self, people):
        return {"name": self.__name, "id": self.__id, "email": self.__email}
        
    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["id"], d["email"])
            
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
    
    
class Student(Person):
    def __init__(self, name, id, email, courses):
        super().__init__(name, id, email)
        self.__courses = courses
        
    def add_course(self, course):
        if course in self.__courses:
            print("Course already added")
        else:
            self.__courses.add(course)
            
    def remove_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
        else:
            print("Course not in set")
            
    def list_courses(self):
        return tuple(self.__courses)
        
        
def save_students(path, students):
    path = Path(path)
    data = [s.to_dict() for s in students]
    
    import json
    with path.open("w") as f:
        json.dump(data, f)
        
def load_students(path):
    pass

class DataError(Exception):
    pass


def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def encode_message(msg):
    pass

def decode_message(msg):
    pass

#inputs
name = ui.input("Enter name: ")
email = ui.input("Enter email: ")

def create_student(student):
    pass
    
#button
create = ui.button("Create Student", on_click=create_student)
    
