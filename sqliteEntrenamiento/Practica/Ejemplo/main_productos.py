from Practica.Ejemplo.crud import crear_tabla_productos, agregar_producto, listar_productos

crear_tabla_productos()

agregar_producto("Laptop", 1200.00)
agregar_producto("Smartphone", 800.00)

productos = listar_productos()
print("Productos en la tienda:")
for producto in productos:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")