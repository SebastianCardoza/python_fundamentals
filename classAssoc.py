class User:
    bank_name="Banco del Dojo"
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.cuenta = []
        self.cuenta.append(CuentaBancaria(int_rate=0.02, balance=0))
        self.cuenta.append(CuentaBancaria(int_rate=0.03, balance=0))

    def saludo(self):
        print(f"Hello mah bro, my name is {self.name}")

    def deposito(self, amount, num_cuenta):
        self.cuenta[num_cuenta].deposito(amount)
        return self

    def hacer_retiro(self, amount, num_cuenta):
        self.cuenta[num_cuenta].retiro(amount)
        return self

    def mostrar_balance(self):
        for i in range(len(self.cuenta)):
            print(f"Usuario: {self.name}, Balance {i+1}: {self.cuenta[i].balance}$")

    def transfer(self, other_user, amount, num_cuenta, other_num_cuenta):
        self.cuenta[num_cuenta].balance -=amount
        other_user.cuenta[other_num_cuenta].balance +=amount

class CuentaBancaria:
    nombre_banco = "Banco de Credito del Dojo"
    todas_las_cuentas = []
    def __init__(self, int_rate, balance):
        self.tasa_int = int_rate
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    @classmethod
    def cambiar_nombre_bancario(cls, name):
        cls.nombre_banco = name

    @classmethod
    def todos_los_balances(cls):
        sum = 0
        for i in cls.todas_las_cuentas:
            sum += i.balance
        return sum

    @classmethod
    def mostrar_balances(cls):
        for i in cls.todas_las_cuentas:
            print(f"Balance: {i.balance}, Interes: {i.tasa_int}")

    @staticmethod
    def puede_retirar(balance, amount):
        if balance - amount >= 0:
            return True
        return False

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if CuentaBancaria.puede_retirar(self.balance, amount):
            self.balance -= amount
        return self

    def mostrar_balance(self):
        print(f"Balance: {self.balance}")

    def generar_interes(self):
        if CuentaBancaria.puede_retirar(self.balance, 1):
            self.balance += self.balance*self.tasa_int
        return self

sebastian = User("Sebastian Cardoza", "jscboulangger@hotmail.com")
# Deposito a la cuenta 1
sebastian.deposito(100, 0)
# No se podra hacer el retiro ya que la cuenta 2 esta en 0 por lo tanto solo se depositara los 200
sebastian.hacer_retiro(200, 1).deposito(200,1)

sebastian.mostrar_balance()