from mascota import Perro, Gato
class Ninja:
    def __init__(self, nombre, apellido, premios, comida_mascota, mascotas):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascotas=mascotas
    def chequear_mascotas(self):
        for i in self.mascotas:
            i.mostrar_salud_energia()
    def caminar(self):
        for i in self.mascotas:
            i.jugar()
    def alimentar(self):
        for i in self.mascotas:
            i.comer()
    def bañar(self):
        for i in self.mascotas:
            i.ruido()


kakashi = Ninja("kakashi", "sensei", 8, 20, [Perro("Fido", "Siberiano", "Croquetas"), Gato("Michifusina", "Callejera linda", "Atun")])
kakashi.alimentar()
kakashi.caminar()
kakashi.chequear_mascotas()
kakashi.bañar()
