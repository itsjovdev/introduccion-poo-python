#Para empezar esta seria de guia de PPO, vamos a crear una clase simple llamada Car que representara un coche con atributos basicos como marca, modelo y año.

class Car:
    #El constructor __init__ es el constructor: se ejecuta al crear un nuevo objeto
    def __init__(self, manufacturer = '', model = None, color = '', cylinder = 0.00):
        #Los atributos con doble guion bajo (__) son privados.
        #Esto significa que no pueden ser accedidos ni modificados directamente desde fuera de la clase.
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        #Un atributo con un guion bajo (_) es protegido.
        #Esto indica que no debe ser accedido directamente desde fuera de la clase, pero puede ser accedido por clases derivadas.
        self.__other = 'motor'
     
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
    
    
    #Metodo especial para convertir el objeto a una cadena de texto
    def __str__(self):
        return f'Car(manufacturer={self.__manufacturer}, model={self.__model}, color={self.__color}, cylinder={self.__cylinder})' 
    #Metodo especial para representar el objeto de manera oficial
    def __repr__(self):
        return f'Car(manufacturer={self.__manufacturer}, model={self.__model}, color={self.__color}, cylinder={self.__cylinder})'
    
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

#Creamos un objeto de la clase Car
car = Car("subaru")
#Cambiamos el color del coche usando el metodo set_color
car.set_color("Red")  
#Cambiamos el modelo del coche usando el metodo set_model
car.set_model("Impreza")

#Cambiamos el valor del atributo cylinder usando el decorador property
car.cylinder = 2.0
car.model = "wrx"

#Mostramos los detalles del objeto car
print(car.get_color())
print(car.details())
print(f'Este printa desde el metodo __str__ \n {car}')

#Creamos otro objeto de la clase Car
print("-----Nuevo objeto mazda-----")
mazda = Car()
mazda.cylinder = 3.0
print(mazda.details())
print(mazda.cylinder)
