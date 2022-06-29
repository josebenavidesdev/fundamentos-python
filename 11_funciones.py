# Una funcion es un bloque de codigo reutilizable que realiza una sola tarea
# especifica

notas = [11, 15, 10, 8, 20]

def obtener_promedio(notas):
    suma = sum(notas)
    cantidad = len(notas)
    promedio = suma / cantidad
    return promedio

promedio_de_notas = obtener_promedio(notas)

print(promedio_de_notas)
