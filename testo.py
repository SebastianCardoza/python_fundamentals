def contadorLetras(palabra):
    result={}
    for letra in palabra:
        result[letra]=0

    for letra in palabra:
        for key in result.keys():
            if letra == key:
                result[letra] += 1
                continue
    
    print(result)
    

contadorLetras("momomol")