from enum import Enum

#La clase Constants almacena constantes de la aplicacion, la direncia es que
#las clases Enum permiten definir un conjunto de valores( pertenecen por ejemplo todos son colores) constantes con nombres legibles.
class Color(Enum):
    RED = 'Rojo desde la clase Color'
    WHITE = 'Blanco'
    GRAY = 'Gris'
    BLUE = 'Azul'
    BLACK = "negro" 