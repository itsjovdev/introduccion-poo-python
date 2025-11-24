from car import Car

Car.set_license_plate_color('blanco')

car = Car().empty()
print(car)

print("===============================")
car1 = Car.basic("mazda", "3")
print(car1)

print("===============================")
car2 = Car.with_color("citroen", "c3", "gris")
print(car2)

print("===============================")
car3 = Car.with_cylinder("subaru", "legacy", "azul", 1.5)
print(car3)

print("===============================")
car4 = Car.full_spec("mazda", "bt-50", "azul", 3.0, 50.00)
print(car4)

print("===============================")
car5 = Car.only_tank("subaru", "impresa", 50.00)
print(car5)

print("===============================")
car6 = Car.only_color("ford", "rojo")
print(car6)

# accedemos al atributo estatico
print(Car.get_license_plate_color())