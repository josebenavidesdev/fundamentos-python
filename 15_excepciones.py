"""
SyntaxError
Error en la sintaxis del programa. Ocurre cuando no se siguen las reglas
formales para escribir codigo en python

Excepcion
Es un error detectado durante la ejecucion de un programa

try:
    Intenta ejecutar este codigo
except:
    Si ocurre una excepcion, detente inmediatamente y ejecuta este codigo
"""

# IndexError: cuando intentamos acceder a un indice que esta fuera de rango
# KeyError: cuando intentamos acceder a una clave que no existe en un diccionario
# NameError: cuando el nombre de una variable no se reconoce
# ZeroDivisionError: division por cero
# RecursionError: recursion infinita ya que nunca se llega al caso base

try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = num1 / num2

    print(f"{num1} / {num2} = {resultado}")
except ValueError as e:
    print(e)
    print("Ingrese solo numeros!")
except ZeroDivisionError as e:
    print(e)
    print("Alerta, Excepcion Division por Cero!")
finally:
    print("Fin")
