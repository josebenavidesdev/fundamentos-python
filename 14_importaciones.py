# Modulo: Es un archivo python que contiene definiciones y sentencias
# Importacion: Es una sentencia que da acceso a las funciones y constantes
# definidas en el modulo importado
# Los paquetes deben contener un archivo __init__.py

"""
import math as matematicas  # importando todo el modulo

resultado = matematicas.pow(9, 2)

print(resultado)  # 81.0
"""

"""
from math import pow  # importando solo algo especifico

print(pow(5, 2))  # 25.0
"""

# importacion de un archivo que se encuentra en la misma ruta
# import matematicas as mate
from matematicas import sumar, restar

print(sumar(10, 20))  # 30
print(restar(10, 20))  # -10

from paquete.funciones_math import saludo, calcular_factorial

print(calcular_factorial(5))  # 120
print(saludo)  # Hola Python

from paquete.sub_paquete.fibo import fibonacci

print(fibonacci(7))  # 13
