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
    
    print('imprimiendo datos en común del tipo persona:')
    print(f'Nombre: {person.first_name}, apellido: {person.last_name}, email: {person.email}')
    #Si la persona es un student, accedemos a los atributos de student
    if isinstance(person, Student):
        print('imprimiendo datos específicos del tipo student:')
        print(f'Institucion: {person.institution}')
        print(f'Math grade: {person.math_grade}')
        print(f'History grade: {person.history_grade}')
        print(f'Language grade: {person.language_grade}')
        #Si la persona es un international student, accedemos a los atributos de international student
        if isinstance(person, InternationalStudent):
            print('imprimiendo datos específicos del tipo international student:')
            print(f'Foreign language grade: {person.foreign_language_grade}')
            print(f'Country: {person.country}')
        
        print('---------------------------------SOBRE ESCRITURA METODO CALCULAR PROMEDIO ------------------------------------------')
        print(f'Promedio: {person.calculate_average()}')
        
        print('---------------------------------SOBRE ESCRITURA METODO write_blackboard ------------------------------------------')
        print(person.write_blackboard())
    #Si la persona es un teacher, accedemos a los atributos de teacher
    if isinstance(person, Teacher):
        print('imprimiendo datos específicos del tipo teacher:')
        print(f'Asignatura: {person.subject}')
        
    print('----------------------------------SOBRE ESCRITURA METODO GREET----------------------------------------------')
    print(person.greet())
        
    print('----------------------------------SOBRE ESCRITURA METODO SPEAK----------------------------------------------')
    print(person.speak())
    
        

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