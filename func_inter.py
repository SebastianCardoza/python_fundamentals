# 1. Actualizar valores de listas y diccionarios

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
estudiantes[0]["last_name"]="Bryant"
directorio_deportes["fútbol"][0]="Andres"
z[0]["y"]=30

# 2. Iterar sobre un diccionario
def iterateDictionary(some_list):
    for some_dict in some_list:
        tbprinted = ""
        for k, v in some_dict.items():
            if k == "last_name":
                tbprinted += f"{k} - {v}"
            else:
                tbprinted += f"{k} - {v}, "
        print(tbprinted)

iterateDictionary(estudiantes)
print("")

# 3. Obtener valores de lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for some_dict in some_list:
        for k, v in some_dict.items():
            if k == key_name:
                print(f"{v}")

iterateDictionary2("first_name", estudiantes)
print("")

# 4. Iterar a traves de un diccionario de listas
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for k, v in some_dict.items():
        print(str(len(v))+" "+k.upper())
        for i in v:
            print(i)
        print("")
printInfo(dojo)