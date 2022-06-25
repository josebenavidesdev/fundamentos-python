# Coleccion de pares clave-valor
# Las claves deben ser unicas e inmutables
# Los valores asociados pueden ser de cualquier tipo
# Los pares clave-valor pueden ser modificados, añadidos y eliminados

usuario = {"nombre": "luis", "edad": 29, "correo": "luis@python.com"}

print(usuario["nombre"])  # luis
print(usuario["edad"])  # 29
print(usuario.get("correo"))  # luis@python.com
print(usuario.get("apellido"))  # None

# agregando o actualizando un nuevo par clave-valor
usuario["apellido"] = "Vega"
print(usuario["apellido"])  # Vega

# remover par clave-valor
del usuario["apellido"]
print(usuario.get("apellido"))  # None

# confirmar clave
print("nombre" in usuario)  # True
print("apellido" in usuario)  # False
