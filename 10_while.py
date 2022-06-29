# Programa para sumar hasta el n número natural

suma = 0
i = 1

numero = int(input("Ingrese un número: "))

while i <= numero:
    suma += i
    i += 1  # actualizamos el contador

print("La suma es: ", suma)
