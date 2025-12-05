import json
from pathlib import Path

class Course:
    def __init__(self, code, title, credits):
        self._code = code
        self._title = title
        self._credits = credits
        
    def get_credits(self):
        return self._credits
    
    def set_credits(self, new_credits):
        try:
            if 1 <= new_credits <= 5:
                self._credits = new_credits
        except ValueError as e:
            print(e)
    
    def to_dict(self):
        return {"code": self._code, "title": self._title, "credits": self._credits}
    
def save_courses(filename, courses):
    data = [c.to_dict() for c in courses]
    path = Path(filename)
    
    with path.open("w") as f:
        json.dump(data, f, indent=4)
        
def load_courses(filename):
    path = Path(filename)
    if not path.exists():
        print("File not found")
        return []
    
    with path.open("r") as f:
        data = json.load(f)     # list of dicts
        
    courses = []
    for d in data:
        course = Course(d["code"], d["title"], d["credits"])
        courses.append(course)
        
    return courses
            
c1 = Course("CS101", "Intro to CS", 4)
c2 = Course("MATH200", "Calculus II", 3)

Course.save_courses("courses.json", [c1, c2])

loaded = Course.load_courses("courses.json")

for c in loaded:
    print(c._code, c._title, c._credits)
