from car import Car

#Creamos un objeto de la clase Car
car = Car("subaru")
#Cambiamos el color del coche usando el metodo set_color
car.set_color("Gris")  
#Cambiamos el modelo del coche usando el metodo set_model
car.set_model("Impreza")
#Cambiamos el valor del atributo cylinder usando el decorador property
car.cylinder = 1.5
car.model ="Impreza modificado"


#Mostramos los detalles del objeto car
print(car.get_color())
print(car.details())
print(car.accelerate_and_brake(2500, 80))


#Creamos otro objeto de la clase Car
print("\n -----Nuevo objeto mazda-----")
mazda = Car('mazda', '3', 'blanco', 2.0)
mazda.cylinder = 3.0
#Mostramos los detalles del objeto mazda
print(mazda.details())
print(mazda.cylinder)
print(car)
print(repr(mazda))
print(mazda.accelerate(3000, 100))
print(mazda.brake())

#Calculamos el consumo de combustible
print(f'Kilometros por litros: {mazda.calculate_consumption(300, 0.60)}')

print(f'Kilometros por litros: {mazda.calculate_consumption(300, 60)}')