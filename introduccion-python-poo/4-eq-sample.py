from car import Car
from datetime import date

car = Car.full_spec("mazda", "bt-50", "azul", 3.0, 50.00)
car2 = Car.full_spec("mazda", "bt-50", "azul", 3.0, 50.00)
car3 = car 

date_now = date.today()

print(car is car2)  # False, porque el is compara la misma istancia en memoria
print(car == car2)  # True, porque tienen el mismo modelo y fabricante, compara por valor
print(car.__eq__(car2))
#Ya hemos hecho una validacion en el metodo __eq__ por lo tanto retornara False
print(car == date_now)