from animales import Oso, Buho, Elefante

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animales = []
    
    def agregar_animales(self, *animales):
        for animal in animales:
            if animal["tipo"] == "oso":
                self.animales.append(Oso(animal["nombre"],animal["edad"]))
            elif animal["tipo"] == "buho":
                self.animales.append(Buho(animal["nombre"],animal["edad"]))
            elif animal["tipo"] == "elefante":
                self.animales.append(Elefante(animal["nombre"],animal["edad"]))

    def mostrar_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animales:
            animal.mostrar_info()

zoo_york = Zoo("Zoo York")
pulgoso = {"nombre":"Pulgoso", "tipo": "oso", "edad": "26"}
wise = {"nombre":"Wise", "tipo": "buho", "edad": "1000"}
godo = {"nombre":"Godo", "tipo": "elefante", "edad": "120"}

zoo_york.agregar_animales(pulgoso)
zoo_york.mostrar_info()
zoo_york.agregar_animales(wise, godo)
zoo_york.mostrar_info()
