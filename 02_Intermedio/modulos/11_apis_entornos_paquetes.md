# 11 - APIs, entornos y paquetes

## Paquetes

Python trae una biblioteca estandar grande, pero tambien puedes instalar paquetes.

```powershell
python -m pip install requests
```

## Entornos virtuales

Un entorno virtual separa dependencias por proyecto.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests
```

Guardar dependencias:

```powershell
python -m pip freeze > requirements.txt
```

Instalar dependencias guardadas:

```powershell
python -m pip install -r requirements.txt
```

## APIs

Una API permite comunicarse con otro sistema.

Ejemplo con `urllib`, que viene incluido:

```python
import json
from urllib.request import urlopen

url = "https://api.github.com"

with urlopen(url) as respuesta:
    datos = json.loads(respuesta.read().decode("utf-8"))

print(datos)
```

## Buenas practicas

- No pongas claves secretas directamente en el codigo.
- Usa variables de entorno para secretos.
- Maneja errores de red.
- Guarda datos importantes en archivos o base de datos.

