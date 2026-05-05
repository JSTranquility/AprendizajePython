# 08 - Programacion orientada a objetos

La programacion orientada a objetos permite modelar cosas con datos y comportamiento.

## Clase y objeto

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"

persona = Persona("Ana", 25)
print(persona.saludar())
```

## Cuando usar clases

Usa clases cuando tienes entidades con estado y comportamiento:

- Usuario
- Cuenta bancaria
- Producto
- Tarea
- Factura

## Metodos

Un metodo es una funcion dentro de una clase.

```python
class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto
```

## Herencia

```python
class Animal:
    def hablar(self):
        return "sonido"

class Perro(Animal):
    def hablar(self):
        return "guau"
```

No uses herencia por costumbre. Muchas veces una funcion o composicion simple es mejor.

