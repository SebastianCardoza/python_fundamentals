from operator import length_hint


def countdown(num):
    for i in range(num, -1, -1):
        print(i)
countdown(5)

def imprimir_y_devolver(num1, num2):
    print(num1)
    return num2
print(imprimir_y_devolver(1,2))

def primero_mas_longitud(list):
    return len(list) + list[0]
print(primero_mas_longitud([1,2,3,4,5]))

def valores_mayores_al_segundo(lista):
    if len(lista) < 2:
        return False
    nuevaLista = []
    for i in lista:
        if i > lista[1]:
            nuevaLista.append(i)
    print(len(nuevaLista))
    return nuevaLista
print(valores_mayores_al_segundo([5,2,3,2,1,4]))

def length_and_value(tam, valor):
    nuevaLista = []
    for x in range(tam):
        nuevaLista.append(valor)
    return nuevaLista
print(length_and_value(4,7))
