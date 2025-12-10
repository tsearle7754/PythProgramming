import json
from pathlib import Path

def add_score(path, name, score):
    path = Path(path)
    if path.exists():
        try:
            with path.open("r") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                data = {}
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    if name not in data:
        data[name] = []
        
    data[name].append(score)
    
    with path.open("w") as f:
        json.dump(data, f, indent=4)
        
        
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
        
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, score):
        if (score < 0) or (score > 100):
            raise ValueError("Grade must be within 0-100")
        self.__grade = score
        
    def info(self):
        return f"Name: {self.__name} | Grade: {self.__grade}"
            