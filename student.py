class Student:
    def __init__(self, _gpa, name):
        self._gpa = _gpa
        self.name = name
        
    def get_gpa(self):
        return self._gpa
    
    def set_gpa(self, new_gpa):
        self._gpa = new_gpa
        
    
        
    