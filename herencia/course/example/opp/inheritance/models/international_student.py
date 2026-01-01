from course.example.opp.inheritance.models.student import Student
from typing import Optional

#Control de tipo, sera hijo de Student
class InternationalStudent(Student):
    def __init__(self, first_name: str | None = None, 
                 last_name: Optional[str] = None,
                 email: Optional[str] = None,
                 institution: str | None = None,
                 math_grade: float = 0.00,
                 language_grade: float = 0.00,
                 history_grade: float = 0.00,
                 country: str | None= None,
                 foreign_language_grade: float  = 0.00):
        super().__init__(first_name, last_name, email, institution, math_grade, language_grade, history_grade)
        self.country = country
        self.foreign_language_grade = foreign_language_grade
    