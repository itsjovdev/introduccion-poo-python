from course.example.opp.inheritance.models.person import Person
from course.example.opp.inheritance.models.student import Student
from course.example.opp.inheritance.models.subject import Subject
from course.example.opp.inheritance.models.teacher import Teacher
from typing import cast

student: Person = Student()
student.first_name = "John"
student.last_name = "Doe"
student.email = "correo@gmail.com"
# student está tipado como Person, por eso desde aquí solo se pueden usar
# los atributos y métodos definidos en Person.
# Con cast lo tratamos como Student para poder acceder
# a sus atributos y métodos específicos.
alumno = cast(Student, student)
alumno.institution = "University XYZ"


teacher = Teacher()
teacher.first_name = "Jane"
teacher.last_name = "Smith"
teacher.email = "profe@gmail.com"
teacher.subject = Subject.MATEMATICS


print(student.first_name, student.last_name, student.email, student.institution)
print(teacher.first_name, teacher.last_name)
print(f"{teacher.subject.name}: {teacher.subject.value}")
print("-----------------------------------------------------------------------")
print(f"student.speack")
print(student.speak())
print("alumno.write_blackboard")
print(alumno.write_blackboard())
print("alumno.speak")
print(alumno.speak())