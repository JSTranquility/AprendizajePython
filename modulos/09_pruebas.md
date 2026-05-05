# 09 - Pruebas

Las pruebas verifican que tu codigo funciona y sigue funcionando cuando lo cambias.

## assert

```python
def sumar(a, b):
    return a + b

assert sumar(2, 3) == 5
```

## unittest

```python
import unittest

def multiplicar(a, b):
    return a * b

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
```

## Que probar

- Casos normales.
- Casos limite.
- Errores esperados.
- Entradas vacias.
- Valores negativos si aplican.

## Diseno para probar

Separa logica de entrada/salida.

Malo para probar:

```python
def pedir_y_sumar():
    a = int(input("a: "))
    b = int(input("b: "))
    print(a + b)
```

Mejor:

```python
def sumar(a, b):
    return a + b
```

