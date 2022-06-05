class Mascota:
    def __init__(self, nombre, tipo, golosinas):
        self.nombre = nombre
        self.tipo = tipo 
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
    
    def dormir(self):
        self.energia += 25
        
    def comer(self):
        self.energia += 5
        self.salud += 10
    
    def jugar(self):
        self.salud += 5
    
    def mostrar_salud_energia(self):
        print(f"{self.nombre} has {self.energia} energy and {self.salud} health")

    def ruido(self):
        print("The pet is happy!!")

class Perro(Mascota):
    def __init__(self, nombre, tipo, golosinas):
        super().__init__(nombre, tipo, golosinas)

    def ruido(self):
        print("Wof wof")
        super().ruido()

class Gato(Mascota):
    def __init__(self, nombre, tipo, golosinas):
        super().__init__(nombre, tipo, golosinas)

    def ruido(self):
        print("Miau Miau")
        super().ruido()


if __name__ == "__main__":
    fido = Perro("Fido", "Siberiano", "Croquetas")
    michifusina = Gato("Michifusina", "Callejera linda", "Atun")
    fido.dormir()
    fido.mostrar_salud_energia()
    michifusina.ruido()
    fido.ruido()