class Cuenta:
    def __init__(self, numero_cuenta: int, documento_identidad: int, nombre: str, saldo: float):
        self._numero_cuenta = numero_cuenta
        self.documento_identidad = documento_identidad
        self.nombre = nombre
        self.saldo = saldo

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    def depositar_dinero(self, cantidad: float):
        retencion = cantidad * 0.19
        cantidad_neta = cantidad - retencion
        self.saldo += cantidad_neta
        print(f"Depósito de ${cantidad:.2f} (Retención 19%: ${retencion:.2f}). Nuevo saldo: ${self.saldo:.2f}")

    def retirar_dinero(self, cantidad: float) -> bool:
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad:.2f}. Nuevo saldo: ${self.saldo:.2f}")
            return True
        print(f"Fondos insuficientes para realizar el retiro. Tienes un saldo de ${self.saldo:.2f}.")
        return False

    def mostrar_datos(self):
        return f"Cuenta: {self._numero_cuenta} | Titular: {self.nombre} (CC: {self.documento_identidad}) | Saldo: ${self.saldo:.2f}"