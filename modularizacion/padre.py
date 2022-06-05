local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"

# print(square(5))
# user = Usuario("Anna")
# print(user.name)
# print(user.di_hola())
if __name__ == "__main__":
    print("el archivo se esta ejecutando directamente")
else:
    print(f"se esta ejecutando porque es importado de otro archivo. El nombre del archivo es: {__name__}")