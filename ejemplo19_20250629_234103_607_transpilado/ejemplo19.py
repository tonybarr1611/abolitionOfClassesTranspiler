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

resultado = 0
def diferencia_absoluta(a, b):
    resultado = 0
    resultado = a - b
    if resultado < 0:
        resultado = resultado * -1
    return resultado
mostrar_mensaje("Resultado de la funcion: ", diferencia_absoluta(5, 12))
mostrar_mensaje("Resultado fuera de la funcion: ", resultado)