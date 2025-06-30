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

def crear_mensaje(nombre, saludo):
    mensaje = ""
    mensaje = saludo + " " + nombre
    return mensaje
mostrar_mensaje(crear_mensaje("Companero", "Hola"))