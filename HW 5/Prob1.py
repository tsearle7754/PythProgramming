class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []
        
    def addStudent(self, student):
        if student not in self.__students:
            self.__students.append(student)
            return f"{student} was added to {self.__courseName}."
        else:
            return f"{student} is already enrolled in {self.__courseName} course."
        
    def getStudents(self):
        return self.__students
    
    def getNumberOfStudents(self):
        return len(self.__students)
    
    def getCourseName(self):
        return self.__courseName
    
    def dropStudent(self, student):
        if student in self.__students:
            self.__students.remove(student)
            return f"{student} was removed from {self.__courseName} course."
        else:
            return f"{student} is not enrolled in {self.__courseName} course."
        
    def __str__(self):
        return f"Name: {self.__courseName}\nStudents: {self.__students}"
    
class InPersonCourse(Course):
    def __init__(self, courseName, roomNumber, schedule, maxSeats):
        super().__init__(courseName)
        self.__roomNumber = roomNumber
        self.__schedule = schedule
        self.__maxSeats = maxSeats
        
    def addStudent(self, student):
        if self.getNumberOfStudents >= self.__maxSeats:
            return f"{self.getCourseName()} course is full."
        
        return super.addStudent(student)
        
    def __str__(self):
        message = super().__str__()
        return f"{message}\nRoom: {self.__roomNumber}\nSchedule: {self.__schedule}\nEnrolled|Max: {self.getNumberOfStudents()}|{self.__maxSeats}"