from operator import truediv


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

        print("FONDOS INSUFICIENTES")
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

if __name__ == "__main__":
    sebastian=CuentaBancaria(0.01, 100)
    daniel=CuentaBancaria(0.02, 200)

    sebastian.deposito(50).deposito(50).deposito(50).retiro(50).generar_interes().mostrar_balance()
    daniel.deposito(300).deposito(300).retiro(50).retiro(50).retiro(50).retiro(50).generar_interes().mostrar_balance()
    CuentaBancaria.mostrar_balances()