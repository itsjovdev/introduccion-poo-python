#Para que sea una clase constante tenemos que importar dataclas
from dataclasses import dataclass
from typing import Final
#El @dataclass es un decorador que se utiliza para crear clases de SOLO datos(atributos) en Python, sin meetodos.
#reduciendo codigo innecesario como __init__, __repr__, __eq__, etc.
# El parametro  frozen=True indica que la clase es inmutable, es decir, no se pueden cambiar los valores de sus atributos una vez creados.
@dataclass(frozen=True)
class Constants:
  # Constantes de clase, son inmutables y se usan para valores que no cambian(aunque realmente en python si se puede cambiar), 
    # se definen en mayusculas
    MAX_SPEED_HIGHWAY: Final[int] = 180
    COLOR_RED = 'RojoX'
    COLOR_WHITE:Final[str] = 'Blanco desde constants'
    COLOR_GRIS:Final[str] = "Gris"
    COLOR_BLUE:Final[str] = "Azul"
    COLOR_BLACK:Final[str] = "Negro"
    
    