from course.example.opp.inheritance.models.person import Person

class Student(Person):

    def __init__(self):
        super().__init__()
        self.institution = None
        self.math_grade = None
        self.language = None
        self.history = None
        
    def speak(self):
        print('El alumno hace una pregunta al profesor')
        
    def write_blackboard(self):
        print('El alumno desarrolla un tema en la pizarra')