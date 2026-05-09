from course.example.opp.inheritance.models.person import Person
from typing import Optional

class Student(Person):

    def __init__(self, first_name: str | None = None, 
                 last_name: Optional[str] = None,
                 email: Optional[str] = None,
                 institution: str | None = None,
                 math_grade: float = 0.00,
                 language_grade: float = 0.00,
                 history_grade: float = 0.00):
        
        super().__init__(first_name, last_name, email)
        self.institution = institution
        self.math_grade = math_grade
        self.language_grade = language_grade
        self.history_grade = history_grade
        
    def speak(self):
        return 'El alumno hace una pregunta al profesor'
        
    def write_blackboard(self):
        return 'El alumno desarrolla un tema en la pizarra'
    
    def greet(self):
        return f"Hola, soy un estudiante de {self.first_name} y estudio en {self.institution}"
    
    def calculate_average(self):
        return (self.math_grade + self.language_grade + self.history_grade) / 3
    
    def __str__(self):
        return (super().__str__() +
            f'\n institución= {self.institution},'
            f'nota matemática= {self.math_grade},'
            f'nota idioma= {self.language_grade},'
            f'nota historia  = {self.history_grade},'
            f'promedio = {self.calculate_average()}')
        