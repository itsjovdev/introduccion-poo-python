#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Car que representara un coche con atributos basicos como marca, modelo y año.
class Car:
    #El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, manufacturer: str | None = None , 
                 model: str | None =  None, 
                 color: str | None = None, 
                 cylinder: float | None = 0.00,
                 tank_capacity: float | None = 40.00
                 ):
        #Los atributos con doble guion bajo (__) son privados.
        #Esto significa que no pueden ser accedidos ni modificados directamente desde fuera de la clase.
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        #Un atributo con un guion bajo (_) es protegido.
        #Esto indica que no debe ser accedido directamente desde fuera de la clase, pero puede ser accedido por clases derivadas.
        self.__other = 'motor'
        
        # capacidad del tanque en litros
        self.__tank_capacity = tank_capacity
        
    @classmethod
    def empty(cls):
        return cls()
    
    @classmethod
    def basic(cls, manufacturer: str, model: str):
        return cls(manufacturer, model)
    
    @classmethod
    def with_color(cls, manufacturer: str, model: str, color: str):
        return cls(manufacturer, model, color)
    
    @classmethod
    def only_color(cls, manufacturer: str,  color: str):
        return cls(manufacturer, None, color)
    
    @classmethod
    def with_cylinder(cls, manufacturer: str, model: str, color: str, cylinder: float):
        return cls(manufacturer, model, color, cylinder)
    
    @classmethod
    def full_spec(cls, manufacturer: str, model: str, color: str, cylinder: float, tank_capacity: float):
        return cls(manufacturer, model, color, cylinder, tank_capacity)
    
    @classmethod
    def only_tank(cls, manufacturer: str, model: str, tank_capacity: float):
        return cls(manufacturer, model, None, None, tank_capacity)
    
    def set_model(self, value):
        self.__model = value
    
    def get_model(self):
        return self.__model
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value
    
    def set_color(self, value):
        self.__color = value 
    
    def get_color(self):
        return self.__color
    
    @property
    def cylinder(self):
        return self.__cylinder
    
    @cylinder.setter
    def cylinder(self, value):
        self.__cylinder = value
        
    #metodo para mostrar los detalles del coche
    #No es recomendable usar print dentro de los metodos, ya que deben centrarse en devolver datos, no en mostrarlos
    #Como en este metodo no imprime nada, para que se pueda devolver valores cuando le pasamos al objeto se necesitara usar print()
    #cuando lo llamemos desde el objeto para mostrar su valor en consola.
    def details(self):
        detail = f'manufacturer = {self.__manufacturer}\n'
        detail += f'model = {self.__model}\n'
        detail += f'color = {self.__color}\n'
        detail += f'cylinder = {self.__cylinder}\n'
        return detail
    
    def accelerate(self, rpm, speed):
        return f"El auto {self.__manufacturer} esta acelerando a {rpm} rpm y {speed} km/h"
        
    def brake(self):
        return f"El auto {self.__manufacturer} {self.__model} esta frenando"
    
    def accelerate_and_brake(self, rpm, speed):
        acceleration = self.accelerate(rpm, speed)
        braking = self.brake()
        return f"{acceleration}\n{braking}"
    
    #Metodo que calculara cuantos kilometros puede recorrer el coche por litro de combustible
    def calculate_consumption(self, km, fuel_percentage):
        if isinstance(fuel_percentage, int):
            fuel_percentage = fuel_percentage / 100.00
        return km / (fuel_percentage * self.__tank_capacity)
    
    
    #Metodo especial para convertir el objeto a una cadena de texto
    def __str__(self):
        return f'Car(manufacturer={self.__manufacturer}, model={self.__model}, color={self.__color}, cylinder={self.__cylinder}, tank_capacity={self.__tank_capacity})' 
    #Metodo especial para representar el objeto de manera oficial, una versión mas tecnica
    def __repr__(self):
        return f'{{manufacturer:{self.__manufacturer}, model:{self.__model}, color:{self.__color}, cylinder:{self.__cylinder} , tank_capacity:{self.__tank_capacity}}}'
