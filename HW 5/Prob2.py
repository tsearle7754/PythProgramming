from Prob1 import Course
from Prob1 import InPersonCourse

class Department:
    def __init__(self, departmentName):
        self.__departmentName = departmentName
        self.__courses = []
        
    def addCourse(self, course: InPersonCourse):
        if course not in self.__courses:
            self.__courses.append(course)
            return f"{course.getCourseName()} was added to {self.__departmentName} department."
        else:
            return f"{course.getCourseName()} is already in {self.__depatmentName} department."
        
    def getCourses(self):
        return self.__courses
    
    def getCourse(self, courseName):
        for course in self.__courses:
            if course.getCourseName() == courseName:
                return course
        return None
    
    def getTotalStudents(self):
        unique_students = set()
        for course in self.__courses:
            for student in course.getStudents():
                unique_students.add(student)
        return len(unique_students)
                
    def getDepartmentStudents(self):
        unique_students = set()
        for course in self.__courses:
            unique_students.update(course.getStudents())
        return sorted(unique_students)
        
    def addStudentToCourse(self, student, courseName):
        course = self.getCourse(courseName)
        if course is None:
            print(f"Course: {courseName} not found in department.")
            return
        course.addStudent(student)
        
    def dropStudentFromCourse(self, student, courseName):
        course = self.getCourse(courseName)
        if course is None:
            print(f"Course: {courseName} not found in department.")
            return
        course.dropStudent(student)
        
    def __str__(self):
        course_names = [course.getCourseName() for course in self.__courses]
        students = self.getDepartmentStudents()
        
        return (
            f"Department: {self.__departmentName}\n"
            f"Courses: {', '.join(course_names)}\n"
            f"Students: {', '.join(students)}"
        )