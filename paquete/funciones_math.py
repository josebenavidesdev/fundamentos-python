saludo = "Hola Python!"

def calcular_factorial(numero):
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    return factorial
