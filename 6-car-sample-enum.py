from constants import Constants
from car import Car
from color import Color

Car.set_license_plate_color(Constants.COLOR_WHITE)

car = Car().empty()
print(car)

print("===============================")
car1 = Car.basic("mazda", "3")
print(car1)

print("===============================")
#para usar el enum, accedemos al valor con .value o en el str del metodo especial lo manejamos con isinstance
car2 = Car.with_color("citroen1", "c3", Color.RED)
print(car2)

print("===============================")
car3 = Car.with_cylinder("subaru", "legacy", Constants.COLOR_BLUE, 1.5)
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

speed_max_highway = Constants.MAX_SPEED_HIGHWAY
print(f"La velocidad maxima en carretera es: {speed_max_highway} km/h")
# tambien podemos imprimir directamente con la clase
print(Constants.MAX_SPEED_HIGHWAY)

Constants.MAX_SPEED_HIGHWAY = 400
print(Constants.MAX_SPEED_HIGHWAY)

#Los enumarados (Emun) tambien  son iterables
for color in Color:
    print(f'Color: {color.name}, Valor: {color.value}')