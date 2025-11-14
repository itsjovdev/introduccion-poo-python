#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Vehicle que representara un coche con atributos basicos como marca, modelo y año.
class Vehicle:
    
    # El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto.
    # Usamos *args para permitir que la clase reciba un número variable de argumentos.
    # Esto es útil en esta guía porque estamos enseñando cómo Python maneja parámetros dinámicos.
    def __init__(self, *args, **kwargs):
        #Los atributos con doble guion bajo (__) son privados.
        #Esto significa que no pueden ser accedidos ni modificados directamente desde fuera de la clase.
        self.manufacturer = None
        self.model = None
        self.color = None
        self.cylinder = None        
        self.tank_capacity = None
    
        args_name = ['manufacturer', 'model', 'color', 'cylinder', 'tank_capacity']
        for name, value in zip(args_name, args):
            setattr(self, name, value)

        # kwargs permite pasar argumentos por nombre, por ejemplo:
        # Vehicle(color="Rojo", cylinder=2.0)
        #
        # Si kwargs contiene un valor para uno de los atributos, lo sobrescribe.
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in args_name:
                    setattr(self, key, value)
                else:
                    raise TypeError(f"Argumento invalido: {key}")
            # if 'manufacturer' in args_name:
            #     self.manufacturer = kwargs.get('manufacturer')
            # if 'model' in args_name:
            #     self.model = kwargs.get('model')
            # if 'color' in args_name:
            #     self.color = kwargs.get('color')
            # if 'cylinder' in args_name:
            #     self.cylinder = kwargs.get('cylinder')
            # if 'tank_capacity' in args_name:
            #     self.tank_capacity = kwargs.get('tank_capacity')
            
            
        #total = len(args)
        # if total == 0:
        #     # No se proporcionaron argumentos, todos los atributos se establecen en None
        #     pass
        # elif total == 1:
        #     self.manufacturer = args[0]
        # elif total == 2:
        #     self.manufacturer, self.model = args
        # elif total == 3:
        #     self.manufacturer, self.model, self.color = args
        # elif total == 4:
        #     self.manufacturer, self.model, self.color, self.cylinder = args
        # elif total == 5:
        #     self.manufacturer, self.model, self.color, self.cylinder, self.tank_capacity = args
        # else:
        #     raise TypeError("Invalido cantidad de argumentos: esperado entre 0 -5, fueron {total}")
        
        
        
    def __str__(self):
        return (f"Manufacturer: {self.manufacturer}, Model: {self.model}, Color: {self.color}, "
                f"Cylinder: {self.cylinder}, Tank Capacity: {self.tank_capacity}")