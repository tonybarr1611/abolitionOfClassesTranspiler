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

def promedio(var_a, var_b, var_c):
    resultado = 1.1
    resultado = var_a + var_b + var_c / 3.0
    return resultado
mostrar_mensaje(promedio(3.5, 4.0, 5.5))