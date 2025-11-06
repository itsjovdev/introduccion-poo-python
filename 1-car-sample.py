#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Car que representara un coche con atributos basicos como marca, modelo y año.

class Car:
    #El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, manufacturer = '', model = None, color = '', cylinder = 0.00):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cylinder = cylinder
        
    def details(self):
        
        print(f'manufacturer = {self.manufacturer}')
        print(f'model = {self.model}')
        print(f'color = {self.color}')
        print(f'cylinder = {self.cylinder}')
        
#Creamos un objeto de la clase Car
car = Car()

#Le pasamos datos al objeto car
car.manufacturer = 'Toyota'
car.model = 'Corolla'
car.color = 'Red'
car.cylinder = 1.8
car.details()

#Creamos otro objeto de la clase Car
mazda = Car()
mazda.manufacturer = 'Mazda'
mazda.model = 'CX-5'
mazda.color = 'Blue'
mazda.cylinder = 2.5
mazda.details()

#Creamos otro objeto de la clase Car, esto es otra forma de agregar datos al objeto car al momento de crearlo
chevrolet = Car("Chevrolet", "Camaro", "Yellow", 3.6)
chevrolet.details()