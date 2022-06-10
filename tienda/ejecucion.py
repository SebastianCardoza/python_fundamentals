import tienda
from producto import Producto

tiendita = tienda.Tienda("Tiendita de Don Pepe")
globopop = Producto("Globo pop", 2, "Golosinas")
chocman = Producto("Chocman", 3, "Golosinas")
rocklets = Producto("Rocklets", 1, "Golosinas")
lechuga = Producto("Lechuga", 5, "Verduras")
apio = Producto("Apio", 4, "Verduras")
coliflor = Producto("coliflor", 6, "Verduras")
productos = {
    globopop, chocman, rocklets, lechuga, apio, coliflor
}

for producto in productos:
    tiendita.agregar_producto(producto)

tiendita.mostrar_productos()
print(" ")
tiendita.vender_producto(4)
print(" ")
tiendita.inflacion(0.5)
tiendita.mostrar_productos()
print(" ")
tiendita.hacer_liquidacion(0.2, "Verduras")
tiendita.mostrar_productos()




