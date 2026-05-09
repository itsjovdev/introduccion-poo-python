from course.example.opp.inheritance.models.person import Person
from course.example.opp.inheritance.models.student import Student
from course.example.opp.inheritance.models.subject import Subject
from course.example.opp.inheritance.models.teacher import Teacher
from course.example.opp.inheritance.models.international_student import (
    InternationalStudent,
)

from typing import cast, List

#Esta es una funcion que recibe un objeto de tipo Person(student, teacher, international student) e imprimira segun el tipo de persona que sea, accediendo a los atributos comunes y especificos de cada tipo de persona
def printPerson(person: Person):
    print(person)
    
# Creación de instancias de cada tipo de persona
student = Student("john", "doe", "email@gmail.com", "institution XYZ")
student.language_grade = 9.00
student.history_grade = 8.50
student.math_grade = 7.75


international_student = InternationalStudent(
    "mark",
    "lee",
    "mark@email.com",
    "global institute",
    math_grade=8.75,
    language_grade=9.00,
    history_grade=9.25,
    country="Canada",
    foreign_language_grade=9.50,
)

teacher = Teacher("Jane", "Alva", "profe@gmail.com", Subject.MATEMATICS)

persons = [student, international_student, teacher]
for p in persons:
    printPerson(p)
    print('----------------------------------------------------------------------------------------')

# O bien lo llamamos directamente a la función printPerson para cada tipo de persona
# Llamadas a la función printPerson para cada tipo de persona
#printPerson(student)
#printPerson(international_student)
#printPerson(teacher)