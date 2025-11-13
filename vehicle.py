#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Vehicle que representara un coche con atributos basicos como marca, modelo y año.
class Vehicle:
    
    # El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto.
    # Usamos *args para permitir que la clase reciba un número variable de argumentos.
    # Esto es útil en esta guía porque estamos enseñando cómo Python maneja parámetros dinámicos.
    def __init__(self, *args):
        #Los atributos con doble guion bajo (__) son privados.
        #Esto significa que no pueden ser accedidos ni modificados directamente desde fuera de la clase.
        self.manufacturer = None
        self.model = None
        self.color = None
        self.cylinder = None        
        self.tank_capacity = None
        total = len(args)
        
        if total == 0:
            # No se proporcionaron argumentos, todos los atributos se establecen en None
            pass
        elif total == 1:
            self.manufacturer = args[0]
        elif total == 2:
            self.manufacturer, self.model = args
        elif total == 3:
            self.manufacturer, self.model, self.color = args
        elif total == 4:
            self.manufacturer, self.model, self.color, self.cylinder = args
        elif total == 5:
            self.manufacturer, self.model, self.color, self.cylinder, self.tank_capacity = args
        else:
            raise TypeError("Invalido cantidad de argumentos: esperado entre 0 -5, fueron {total}")
        
    def __str__(self):
        return (f"Manufacturer: {self.manufacturer}, Model: {self.model}, Color: {self.color}, "
                f"Cylinder: {self.cylinder}, Tank Capacity: {self.tank_capacity}")