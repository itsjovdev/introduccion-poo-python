from vehicle import Vehicle


vehicle = Vehicle()
print(vehicle)

print("===============================")
car = Vehicle("mazda", "3")
print(car)

print("===============================")
car2 = Vehicle("citroen", "c3", "gris")
print(car2)

print("===============================")
car3 = Vehicle("subaru", "legacy", "azul", 1.5)
print(car3)

print("===============================")
car4 = Vehicle("mazda", "bt-50", "azul", 3.0, 50.00)
print(car4)

print("===============================")
car5 = Vehicle("subaru", "impresa", None, None, 50.00)
print(car5)

print("===============================")
car6 = Vehicle("ford", None, "rojo")
print(car6)

print("===============================")
car7 = Vehicle(manufacturer="negro", color = "gris")
print(car7)

print("===============================")
car8 = Vehicle(model="L200", cylinder=2.0)
print(car8)

print("===============================")
car9 = Vehicle()