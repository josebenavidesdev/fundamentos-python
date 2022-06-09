""" OPERADORES ARITMETICOS """
print(15 + 10)  # 25
print(15 + 10.0)  # 25.0
print(2 - 8.9)  # -6.9
print(2 - 8)  # -6
print(-5 * 8)  # -40
print(15 / 5)  # 3.0
# NOTA: el resultado de una division siempre es un número de coma flotante
# 5 / 0 => ZeroDivisionError

print(15 // 5)  # 3, division entera
print(15 // 5.0)  # 3.0
# NOTA: // solo retorna un flotante si al menos uno es flotante, es utilizado
# en el algoritmo de busqueda binaria

print(5 ** 3)  # 125, 5 al cubo
print(5 ** 0)  # 1

# RESTO DE UNA DIVISION
print(15 % 3)  # 0
print(15 % 2)  # 1
print(16 % 6)  # 4

# ORDEN DE OPERACIONES ARITMETICAS (PEMDAS)
# Parentesis, Exponentes, Multiplicacion, Division, Adicion, Sustraccion

# SUMA DE CADENAS
print("Hola " + "Mundo!")  # Hola Mundo!

""" OPERADORES LOGICOS """
print((5 < 6) and (6 > 8))  # False
print((5 < 6) or (6 > 8))  # True
print(not True)  # False

""" OPERADORES RELACIONALES """
print(8 != 8)  # False
print(8 <= 8)  # True

""" OPERADORES DE ASIGNACION """
edad = 21
edad += 4
print(edad)  # 25

edad -= 5
print(edad)  # 20
# -=, /=, //=, +=, *=, **=, %=
