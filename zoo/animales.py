class Animal:
    def __init__(self, tipo, nombre, edad=1):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.salud = 0
        self.felicidad = 0

    def alimentar(self):
        self.salud += 10
        self.felicidad += 10

    def mostrar_info(self):
        print(f"{self.nombre}, edad: {self.edad}, salud: {self.salud}, felicidad: {self.felicidad}")

class Oso(Animal):
    def __init__(self,nombre, edad):
        super().__init__("oso", nombre, edad)
        self.salud = 80
        self.felicidad = 100
        self.pelaje = "marron"
    
    def alimentar(self):
        self.salud += 20
        self.felicidad += 5

class Buho(Animal):
    def __init__(self, nombre, edad):
        super().__init__("buho", nombre, edad)
        self.salud = 70
        self.felicidad = 85
        self.plumaje = "grisaceo"

    def alimentar(self):
        self.salud += 5
        self.felicidad += 15

class Elefante(Animal):
    def __init__(self, nombre, edad):
        super().__init__("elefante", nombre, edad)
        self.salud = 100
        self.felicidad = 120
        self.trompa = "larga"

    def alimentar(self):
        self.salud += 15
        self.felicidad += 20