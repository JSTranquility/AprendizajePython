"""
Ejercicios de funciones y POO.

Ejecuta:
    python ejercicios/03_funciones_poo.py
"""


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto

    def resumen(self):
        return f"{self.titular}: {self.saldo:.2f}"


def aplicar_descuento(precio, porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return precio - (precio * porcentaje / 100)


def ejecutar_pruebas():
    cuenta = CuentaBancaria("Ana", 100)
    cuenta.depositar(50)
    assert cuenta.saldo == 150
    cuenta.retirar(20)
    assert cuenta.saldo == 130
    assert cuenta.resumen() == "Ana: 130.00"
    assert aplicar_descuento(100, 15) == 85

    try:
        cuenta.retirar(1000)
    except ValueError as error:
        assert str(error) == "Fondos insuficientes"
    else:
        raise AssertionError("Se esperaba ValueError")

    print("Todos los ejercicios de funciones y POO pasaron.")


if __name__ == "__main__":
    ejecutar_pruebas()

