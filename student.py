import json
from pathlib import Path

class Student:
    def __init__(self, _gpa, name):
        self._gpa = _gpa
        self.name = name
        
    def get_gpa(self):
        return self._gpa
    
    def set_gpa(self, new_gpa):
        try:
            if 0.0 <= new_gpa <= 4.0:
                self._gpa = new_gpa
        except ValueError:
            return "GPA must be within 0.0 and 4.0"
        
    def to_dict(self):
        return {"name": self.name, "gpa": self._gpa}
    
    
def save_students(filename, students):
    data = [s.to_dict() for s in students]
    path = Path(filename)
    
    with path.open("w") as f:
        json.dump(data, f, indent=4)
    
s1 = Student(3.0, "Alice")
s2 = Student(3.5, "Bob")
s3 = Student(2.0, "Billy")

try:
    s3.set_gpa(1.5)
except ValueError as e:
    print(e)
    
save_students("students.json", [s1, s2, s3])

print("Students succesfully saved.")