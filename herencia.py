from classMethod import CuentaBancaria

class CuentaVitalicia(CuentaBancaria):
    def __init__(self, int_rate, cuenta_ira, balance=0):
        super().__init__(int_rate, balance)
        self.cuenta_ira=cuenta_ira
    # Ya que la funcion retiro es la unica que voy a cambiar usando el concepto de polimorfismo no tengo necesidad de cambiar deposito ni mostrar_balance
    def retiro(self, amount,es_temprano):
        if es_temprano:
            amount *= 1.10
        return super().retiro(amount)

sebastian = CuentaVitalicia(0.01, "cuenta ira", 100)
sebastian.retiro(10, True)
sebastian.deposito(100)
sebastian.mostrar_balance()