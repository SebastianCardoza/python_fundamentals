class User:
    bank_name="Banco del Dojo"
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.balance = 0

    def saludo(self):
        print(f"Hello mah bro, my name is {self.name}")
    def deposito(self, amount):
        self.balance += amount
    def hacer_retiro(self, amount):
        self.balance -= amount
    def mostrar_balance(self):
        print(f"Usuario: {self.name}, Balance: {self.balance}$")
    def transfer(self, other_user, amount):
        self.balance -=amount
        other_user.balance +=amount

sebastian = User("Sebastian Cardoza", "jscboulangger@hotmail.com")
daniel = User("Daniel Barrientos", "nerocpp@hotmail.com")
pepito = User("Pepito Barrientos", "pepcpp@hotmail.com")

sebastian.deposito(40)
sebastian.deposito(40)
sebastian.deposito(40)
sebastian.hacer_retiro(20)
print(sebastian.balance)
print(daniel.balance)
print(pepito.balance)
print("")

daniel.deposito(80)
daniel.deposito(80)
daniel.hacer_retiro(30)
daniel.hacer_retiro(30)
print(sebastian.balance)
print(daniel.balance)
print(pepito.balance)
print("")

pepito.deposito(160)
pepito.hacer_retiro(20)
pepito.hacer_retiro(20)
pepito.hacer_retiro(20)
print(sebastian.balance)
print(daniel.balance)
print(pepito.balance)
print("")

sebastian.transfer(pepito, 30)
print(sebastian.balance)
print(daniel.balance)
print(pepito.balance)
