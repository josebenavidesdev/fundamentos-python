""" Caracteristicas """
# Secuencia ordenada de valores
# Puede contener valores de cualquier tipo
# Cada posicion de la lista esta asociada a un indice
# Es mutable. Puede ser modificada

letras = ["a", "b", "c", "d"]

print(letras[1])  # b
print(letras[-1])  # d
print(letras[0:2])  # ['a', 'b']

letras.append("e")
print(letras[-1])  # e

letras.insert(0, "A")  # insertamos 'A' en la posicion 0
print(letras[0])  # A

letras.remove("A")  # elimina la primera ocurrencia en la lista
# si el metodo remove no encuentra una ocurrencia lanza un ValueError
print(letras)  # ['a', 'b', 'c', 'd', 'e']

# Preguntamos si un elemento se encuentra en la lista
print("Z" in letras)  # False
print("c" in letras)  # True

print(letras.index("c"))  # 2 => indice donde se encuentra el elemento
# si el metodo index no encuentra una ocurrencia lanza un ValueError

letras[0] = "A"  # actualizamos
print(letras)  # ['A', 'b', 'c', 'd', 'e']

letras.reverse()
print(letras)  # ['e', 'd', 'c', 'b', 'A']

# cuantas veces aparece 'e' en la lista
print(letras.count("e"))  # 1

ultimo_elemento_eliminado = letras.pop()
print(ultimo_elemento_eliminado)  # A

# extendemos una lista pasandole otra lista
letras.extend(["f", "g", "h"])
print(letras)  # ['e', 'd', 'c', 'b', 'f', 'g', 'h']

# ordenamos la lista de forma ascendente
letras.sort()
print(letras)  # ['b', 'c', 'd', 'e', 'f', 'g', 'h']

# ordenamos la lista de forma descendente
letras.sort(reverse=True)
print(letras)  # ['h', 'g', 'f', 'e', 'd', 'c', 'b']
