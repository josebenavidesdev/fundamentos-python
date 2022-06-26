# i es una variable de control

for i in range(4):
    print(i)  # 0 1 2 3

for i in range(1, 6):
    print(i)  # 1 2 3 4 5

for i in 0, 1, 2, 3:
    print(i)  # 0 1 2 3

# imprimir numeros pares del 1 al 10
# range(inicio, fin, paso)
for i in range(2, 11, 2):
    print(i)  # 2 4 6 8 10

# ITERABLES: cadenas, listas, tuplas, diccionarios, otros
for char in "Loops":
    print(char)  # L o o p s

for num in [1, 2, 3]:
    print(num)  # 1 2 3

letras = {"a": 1, "b": 2, "c": 3}

for clave in letras.keys():
    print(clave)  # a b c

for valor in letras.values():
    print(valor)  # 1 2 3

for clave, valor in letras.items():
    print(f"{clave}: {valor}")  # a: 1 b: 2 c: 3
