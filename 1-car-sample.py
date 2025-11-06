#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Car que representara un coche con atributos basicos como marca, modelo y año.

class Car:
    #El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, manufacturer = '', model = None, color = '', cylinder = 0.00):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cylinder = cylinder

car = Car()

#Le pasamos datos al objeto car
car.manufacturer = 'Toyota'
car.model = 'Corolla'
car.color = 'Red'
car.cylinder = 1.8

#Mostramos los datos del objeto car
print(f'car.manufacturer: ',  car.manufacturer)
print(f'car.model: ',  car.model)
print(f'car.color: ',  car.color)
print(f'car.cylinder: ',  car.cylinder)
