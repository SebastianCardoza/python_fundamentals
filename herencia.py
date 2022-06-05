from classMethod import CuentaBancaria

class CuentaVitalicia(CuentaBancaria):
    def __init__(self, int_rate, cuenta_ira, balance=0):
        super().__init__(int_rate, balance)
        self.cuenta_ira=cuenta_ira
    def deposito(self, amount):
        return super().deposito(amount)
    def retiro(self, amount,es_temprano):
        if es_temprano:
            amount *= 1.10
        return super().retiro(amount)
    def mostrar_balance(self):
        return super().mostrar_balance()

sebastian = CuentaVitalicia(0.01, "cuenta ira", 100)
sebastian.retiro(10, True)