# Una funcion recursiva consta de dos casos: caso base y caso recursivo
# El caso base hace que la funcion se detenga
# El caso recursivo es el que nos permite descomponer un problema en una
# version mas pequeña de si misma
# 0 ,1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ...
# 0  1  2  3  4  5  6  7   8  ...

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

obtener_numero = fibonacci(7)

print(obtener_numero)  # 13
