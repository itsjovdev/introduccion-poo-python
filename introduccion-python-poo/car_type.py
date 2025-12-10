from enum import Enum

class CarType(Enum):
    SEDAN = ("Sedan", "Auto mediano", 4)
    STATION_WAGON = ("Station wagon", "Auto grande", 4)
    HATCHBACK = ("Hatchback", "Auto compacto", 5)
    PICKUP = ("Pickup", "Camioneta", 4)
    COUPE = ("Coupe", "Auto pequeño", 2)
    CONVERTIBLE = ("Convertible", "Auto deportivo", 2)
    VAN = ("Van", "Auto de transpote o utilitario", 7)
    SUV = ("SUV", "Todo terreno deportivo", 5)
    

    def __init__(self, name, description, door_count):
            self.__name = name
            self.__description = description
            self.__door_count = door_count
        


    @property
    def name_default(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def door_count(self):
        return self.__door_count