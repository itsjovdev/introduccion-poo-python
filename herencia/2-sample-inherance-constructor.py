from course.example.opp.inheritance.models.person import Person
from course.example.opp.inheritance.models.student import Student
from course.example.opp.inheritance.models.subject import Subject
from course.example.opp.inheritance.models.teacher import Teacher
from typing import cast, List

student = Student("john", "doe", "email@gmail.com", "institution XYZ")


teacher = Teacher("Jane", "Alva", "profe@gmail.com", Subject.MATEMATICS)


print("Student:", student.first_name, student.last_name, student.email, student.institution)
print(f"Teacher {teacher.first_name} {teacher.last_name}: {teacher.subject.value}")