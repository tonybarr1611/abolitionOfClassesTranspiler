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

def divisible(dividendo, divisor):
    resultado = 0
    if dividendo % divisor == 0:
        resultado = 1
    else:
        resultado = 0
    return resultado
resultado_divisible = 0
dividendo = 1
divisor = 1
dividendo = opinion_numerica("Ingrese el dividendo: ")
divisor = opinion_numerica("Ingrese el divisor: ")
resultado_divisible = divisible(dividendo, divisor)
mostrar_mensaje(dividendo, " es divisible por ", divisor, ": ", resultado_divisible)