from constants import Constants
from car import Car
from color import Color
from car_type import CarType

Car.set_license_plate_color(Constants.COLOR_WHITE)

car = Car().empty()
print(car)

print("===================")
car1 = Car.basic("mazda", "3")
car1.car_type = CarType.HATCHBACK
print(car1)

print("===============================")
#para usar el enum, accedemos al valor con .value o en el str del metodo especial lo manejamos con isinstance
car2 = Car.with_color("citroen1", "c3", Color.RED)
car2.car_type = CarType.SEDAN
print(car2)

print("===============================")
car3 = Car.with_cylinder("subaru", "legacy", Constants.COLOR_BLUE, 1.5)
car3.car_type = CarType.STATION_WAGON
print(car3)

print("===============================")
car4 = Car.full_spec("mazda", "bt-50", "azul", 3.0, 50.00)
car4.car_type = CarType.SUV
print(car4)

print("===============================")
car5 = Car.only_tank("subaru", "impresa", 50.00)
print(car5)

print("===============================")
car6 = Car.only_color("ford", "rojo")
print(car6)

# accedemos al atributo estatico
print(Car.get_license_plate_color())

speed_max_highway = Constants.MAX_SPEED_HIGHWAY
print(f"La velocidad maxima en carretera es: {speed_max_highway} km/h")
# tambien podemos imprimir directamente con la clase
print(Constants.MAX_SPEED_HIGHWAY)

Constants.MAX_SPEED_HIGHWAY = 400
print(Constants.MAX_SPEED_HIGHWAY)

#Los enumarados (Emun) tambien  son iterables
for color in Color:
    print(f'Color: {color.name}, Valor: {color.value}')
    
#Imprimir detalles del enum CarType
print("Detalles de los tipos de coche:")
print(car1.car_type)
print(car1.car_type.name)
print(car1.car_type.name_default)
print(car1.car_type.description)
print(car1.car_type.door_count)

car_type = car1.car_type

match car_type: 
    case CarType.CONVERTIBLE:
        print("Es un coche descapotable.")
    case CarType.SUV:
        print("Es un SUV.")
    case CarType.PICKUP:
        print("Es una camioneta pickup.")
    case CarType.SEDAN:
        print("Es un sedan.")
    case CarType.HATCHBACK:
        print("Es un hatchback.")

for ct in CarType:
    print(f'Tipo de coche: {ct.name}, Nombre: {ct.name_default}, Descripción: {ct.description}, Número de puertas: {ct.door_count}')