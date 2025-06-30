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


def validar_velocidad(velocidad):
    es_valida = 0
    if velocidad <= 50:
        es_valida = 1
    else:
        es_valida = 0

    return es_valida


def obtener_velocidad_babosa(numero_babosa):
    velocidad = 0
    velocidad_valida = 0

    while velocidad_valida == 0:
        mostrar_mensaje("Ingrese la velocidad de la babosa ", numero_babosa, " (1-50): ")
        velocidad = opinion_numerica("")
        if validar_velocidad(velocidad) == 1:
            velocidad_valida = 1
        else:
            mostrar_mensaje("Error: La velocidad debe estar entre 1 y 50. Intente nuevamente.")


    return velocidad


def determinar_ganador(distancia1, distancia2, distancia3):
    ganador = 1
    if distancia2 > distancia1:
        ganador = 2
    if distancia3 > distancia1:
        if distancia3 > distancia2:
            ganador = 3
    return ganador


def ha_finalizado(distancia1, distancia2, distancia3):
    ha_terminado = 0
    if distancia1 >= 300:
        ha_terminado = 1
    if distancia2 >= 300:
        ha_terminado = 1
    if distancia3 >= 300:
        ha_terminado = 1
    return ha_terminado


def obtener_distancia_guiones(distancia):
    guiones = ""

    while distancia > 0:
        guiones = guiones + "-"
        distancia = distancia - 10

    return guiones


def iniciar_carrera():
    mostrar_mensaje("=== CARRERA DE BABOSAS ===")
    mostrar_mensaje("Bienvenido a la gran carrera revolucionaria de babosas!")
    mostrar_mensaje("")
    velocidad_babosa1 = 0
    velocidad_babosa2 = 0
    velocidad_babosa3 = 0
    velocidad_babosa1 = obtener_velocidad_babosa(1)
    velocidad_babosa2 = obtener_velocidad_babosa(2)
    velocidad_babosa3 = obtener_velocidad_babosa(3)
    mostrar_mensaje("")
    mostrar_mensaje("=== CONFIGURACION DE LA CARRERA ===")
    mostrar_mensaje("Babosa 1 - Velocidad: ", velocidad_babosa1)
    mostrar_mensaje("Babosa 2 - Velocidad: ", velocidad_babosa2)
    mostrar_mensaje("Babosa 3 - Velocidad: ", velocidad_babosa3)
    mostrar_mensaje("")
    tiempo_carrera = 10
    mostrar_mensaje("Â¡La carrera comienza! Duracion: ", tiempo_carrera, " segundos")
    mostrar_mensaje("")
    distancia_babosa1 = 0
    distancia_babosa2 = 0
    distancia_babosa3 = 0
    tiempo_transcurrido = 0

    while ha_finalizado(distancia_babosa1, distancia_babosa2, distancia_babosa3) == 0:
        distancia_babosa1 = distancia_babosa1 + velocidad_babosa1 / 2
        distancia_babosa2 = distancia_babosa2 + velocidad_babosa2 / 2
        distancia_babosa3 = distancia_babosa3 + velocidad_babosa3 / 2
        tiempo_transcurrido = tiempo_transcurrido + 1
        expropiar()
        mostrar_mensaje("=== ESTADO DE LA CARRERA ===")
        mostrar_mensaje("Tiempo transcurrido: ", tiempo_transcurrido, " segundos")
        mostrar_mensaje("Babosa 1 => ", obtener_distancia_guiones(distancia_babosa1))
        mostrar_mensaje("Babosa 2 => ", obtener_distancia_guiones(distancia_babosa2))
        mostrar_mensaje("Babosa 3 => ", obtener_distancia_guiones(distancia_babosa3))
        mostrar_mensaje("")
        dormir(1)

    babosa_ganadora = 0
    expropiar()
    babosa_ganadora = determinar_ganador(distancia_babosa1, distancia_babosa2, distancia_babosa3)
    mostrar_mensaje("LA BABOSA ", babosa_ganadora, " HA GANADO LA CARRERA !!!")
    mostrar_mensaje("")
    mostrar_mensaje("La babosa 1 ha recorrido: ", obtener_distancia_guiones(distancia_babosa1))
    mostrar_mensaje("La babosa 2 ha recorrido: ", obtener_distancia_guiones(distancia_babosa2))
    mostrar_mensaje("La babosa 3 ha recorrido: ", obtener_distancia_guiones(distancia_babosa3))
    return babosa_ganadora

mostrar_mensaje("Iniciando simulador de carrera...")
iniciar_carrera()