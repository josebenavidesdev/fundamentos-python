# Es una estructura de datos inmutable que contiene una secuencia ordenada de
# elementos

numeros = (10, "20", 30, "40", 50)

print(numeros[1])  # 20

print(30 in numeros)  # True

print(numeros.index("40"))  # 3

letras = ("a", "b", "a", "d", "a")

print(letras.count("a"))  # 3
print(letras.count("z"))  # 0
