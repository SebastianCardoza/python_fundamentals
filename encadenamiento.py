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

sebastian.deposito(40).deposito(40).deposito(40).hacer_retiro(20).mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
print("")

sebastian.mostrar_balance()
daniel.deposito(80).deposito(80).hacer_retiro(30).hacer_retiro(30).mostrar_balance()
pepito.mostrar_balance()
print("")

sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.deposito(160).hacer_retiro(20).hacer_retiro(20).hacer_retiro(20).mostrar_balance()
print("")

sebastian.transfer(pepito, 30)
sebastian.mostrar_balance()
daniel.mostrar_balance()
pepito.mostrar_balance()
