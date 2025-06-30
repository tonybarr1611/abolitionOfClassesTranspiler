# Ambiente estándar para Abolition of Classes
import sys

def mostrar_mensaje(*args):
    """Función para mostrar mensajes (equivalente a print)"""
    mensaje = ""
    for arg in args:
        mensaje += str(arg)
    print(mensaje)

def opinion(texto: str = ""):
    """Función para obtener entrada del usuario"""
    if texto:
        print(texto)
    return input()

def opinion_numerica(texto: str = ""):
    """Función para obtener entrada numérica del usuario"""
    if texto:
        print(texto)
    try:
        return int(input())
    except ValueError:
        try:
            return float(input())
        except ValueError:
            return 0

# Código generado por el transpilador

def suma_pares(n):
    suma = 0
    indice = 2
    while indice <= n:
        suma = suma + indice
        indice = indice + 2
    return suma
entrada = 0
entrada = opinion_numerica("Ingrese un numero entero positivo: ")
if entrada < 1:
    mostrar_mensaje("El numero debe ser mayor o igual a 1.")
else:
    mostrar_mensaje("La suma de los numeros pares desde 1 hasta ", entrada, " es: ", suma_pares(entrada))