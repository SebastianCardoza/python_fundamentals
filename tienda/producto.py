class Producto:
    creador_id = 0
    def __init__(self, nombre, precio, categoria):
        Producto.creador_id += 1
        self.id = Producto.creador_id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio *= (1+cambio_porcentaje)
        else:
            self.precio *= (1-cambio_porcentaje)

    def print_info(self):
        print(f"id: {self.id}, nombre: {self.nombre}, precio: {self.precio} $, categoría: {self.categoria}")