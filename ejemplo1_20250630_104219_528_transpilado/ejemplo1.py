# Ambiente estándar para Abolition of Classes
import os
from time import sleep

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
            
def dormir(segundos: int):
    """Función para pausar la ejecución por un número de segundos"""
    sleep(segundos)

def expropiar():
    """Función para limpiar la consola, similar a cls en Windows o clear en Unix."""
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # macOS y Linux
    else:
        _ = os.system('clear')

# Código generado por el transpilador


def factorial(n):
    resultado = 0
    if n == 0:
        resultado = 1
    else:
        factorial_n_menos_1 = 0
        factorial_n_menos_1 = factorial(n - 1)
        resultado = n * factorial_n_menos_1

    return resultado

resultado = 0
resultado = factorial(5)
mostrar_mensaje("El factorial de 5 es: ", resultado)