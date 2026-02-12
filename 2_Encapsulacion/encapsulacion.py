# ================================================
#                 EJEMPLO DE ENCAPSULACIÓN
# ================================================

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto

    def mostrar_info(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo}"


# Programa principal
cuenta = CuentaBancaria("Evelyn", 300)
cuenta.depositar(100)
cuenta.retirar(150)
print(cuenta.mostrar_info())
