from course.example.opp.inheritance.models.person import Person
from course.example.opp.inheritance.models.subject import Subject
from typing import Optional

class Teacher(Person):
    def __init__(self, first_name: str | None = None, 
                 last_name: Optional[str] = None,
                 email: Optional[str] = None,
                 subject: Optional[Subject] = None):
        super().__init__(first_name, last_name, email)
        self.subject = subject