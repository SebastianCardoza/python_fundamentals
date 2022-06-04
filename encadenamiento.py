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
        return self
    def hacer_retiro(self, amount):
        self.balance -= amount
        return self
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
sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
print("")

daniel.deposito(80)
daniel.deposito(80)
daniel.hacer_retiro(30)
daniel.hacer_retiro(30)
sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
print("")

pepito.deposito(160)
pepito.hacer_retiro(20)
pepito.hacer_retiro(20)
pepito.hacer_retiro(20)
sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
print("")

sebastian.transfer(pepito, 30)
sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
