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

def numero_palindromo(numero):
    original = 0
    original = numero
    invertido = 0
    resultado = 0
    while numero > 0:
        digito = 0
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10
    if invertido == original:
        resultado = 1
    else:
        resultado = 0
    mostrar_mensaje("El numero es un palindromo: ", resultado)
    return resultado
numero_palindromo(12321)
numero_palindromo(12345)