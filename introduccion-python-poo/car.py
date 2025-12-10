from typing import Final, Optional
from color import Color
from engine import Engine
from fuel_tank import FuelTank
from car_type import CarType
#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Car que representara un coche con atributos basicos como marca, modelo y año.
class Car:
    
    __license_plate_color = 'Orange'
    
    last_id = 0
    

    #El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, manufacturer: str | None = None,
                 model: str | None =  None, 
                 color: str | Color | None = None, 
                 engine: Optional[Engine]  = None,
                 fuel_tank: Optional[FuelTank]  = None):
        #Los atributos con doble guion bajo (__) son privados.
        #Esto significa que no pueden ser accedidos ni modificados directamente desde fuera de la clase.
        Car.last_id = Car.last_id + 1
        self.__id = Car.last_id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__engine: Optional[Engine] = engine
        #Un atributo con un guion bajo (_) es protegido.
        #Esto indica que no debe ser accedido directamente desde fuera de la clase, pero puede ser accedido por clases derivadas.
        self.__other = 'motor'
        
        # capacidad del tanque en litros
        self.__fuel_tank: FuelTank |None = fuel_tank
        self.__car_type: Optional[CarType]  = None  # Tipo de coche, puede ser asignado posteriormente
        
    @classmethod
    def empty(cls):
        return cls()
    
    @classmethod
    def basic(cls, manufacturer: str, model: str):
        return cls(manufacturer, model)
    
    @classmethod
    def with_color(cls, manufacturer: str, model: str, color: str | Color):
        return cls(manufacturer, model, color)
    
    @classmethod
    def only_color(cls, manufacturer: str,  color: str | Color):
        return cls(manufacturer, None, color)
    
    @classmethod
    def with_cylinder(cls, manufacturer: str, model: str, color: str | Color, cylinder: float):
        return cls(manufacturer, model, color, cylinder)
    
    @classmethod
    def full_spec(cls, manufacturer: str, model: str, color: str | Color, cylinder: float, tank_capacity: float):
        return cls(manufacturer, model, color, cylinder, tank_capacity)
    
    @classmethod
    def only_tank(cls, manufacturer: str, model: str, tank_capacity: float):
        return cls(manufacturer, model, None, None, tank_capacity)
    
    def set_model(self, value):
        self.__model = value
    
    def get_model(self):
        return self.__model
    
    #para trabajar con el atributo estatico
    @classmethod
    def set_license_plate_color(cls, value):
        cls.__license_plate_color = value
    
    @classmethod
    def get_license_plate_color(cls):
        return cls.__license_plate_color
    
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
    def engine(self):
        return self.__engine
    
    @engine.setter
    def engine(self, value):
        self.__engine = value
        
    
    @property
    def car_type(self):
        return self.__car_type
    
    @car_type.setter
    def car_type(self, value):
        self.__car_type = value
        
        
    @property
    def fuel_tank(self):
        return self.__fuel_tank
    
    @fuel_tank.setter
    def fuel_tank(self, value):
        self.__fuel_tank = value
        
    #metodo para mostrar los detalles del coche
    #No es recomendable usar print dentro de los metodos, ya que deben centrarse en devolver datos, no en mostrarlos
    #Como en este metodo no imprime nada, para que se pueda devolver valores cuando le pasamos al objeto se necesitara usar print()
    #cuando lo llamemos desde el objeto para mostrar su valor en consola.
    def details(self):
        detail = f'manufacturer = {self.__manufacturer}\n'
        detail += f'model = {self.__model}\n'
        detail += f'color = {self.__color}\n'
        detail += f'engine = {self.__engine.cylinder if isinstance(self.__engine, Engine) else None}\n'
        detail += f'patente = {Car.__license_plate_color}\n'
        detail += f'id = {self.__id}'
        
        
        
        
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
        return (f'Car(manufacturer={self.__manufacturer}, '
            f'model={self.__model}, color={self.__color.value if isinstance(self.__color, Color) else self.__color}, '
            f'engine_cylinder={self.__engine.cylinder if isinstance(self.__engine, Engine) else None}, '
            f'cylinder={self.__cylinder}, tank_capacity={self.__tank_capacity}, '
            f'license_plate_color={Car.__license_plate_color})'
            f'id = {self.__id}'
            f'car_type={self.__car_type.name if self.__car_type else None}'
            )
    #Metodo especial para representar el objeto de manera oficial, una versión mas tecnica
    def __repr__(self):
        return f'{{manufacturer:{self.__manufacturer},engine = {self.__engine.cylinder if isinstance(self.__engine, Engine) else None},   model:{self.__model}, color:{self.__color}, cylinder:{self.__cylinder} , tank_capacity:{self.__tank_capacity}}}'
    
    #Metodo especial para comparar objetos de la clase Car
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Car):
            return False
        #Compara si el modelo y el fabricante seran iguales
        return self.__model == other.__model and self.__manufacturer == other.__manufacturer