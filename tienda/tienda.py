class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def agregar_producto(self, nuevo_producto):
        self.lista.append(nuevo_producto)

    def vender_producto(self, id):
        for i in range(len(self.lista)):
            if self.lista[i].id == id:
                self.lista[i].print_info()
                self.lista.pop(i)
                break

    def inflacion(self, porcentaje_numero):
        for i in range(len(self.lista)):
            self.lista[i].actualizar_precio(porcentaje_numero, True)

    def hacer_liquidacion(self, porcentaje_numero, categoria):
        for i in range(len(self.lista)):
            if self.lista[i].categoria == categoria:
                self.lista[i].actualizar_precio(porcentaje_numero, False)
    
    def mostrar_productos(self):
        for producto in self.lista:
            producto.print_info()