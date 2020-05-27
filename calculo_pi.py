import random
import math
from estadisticas import desviacion_estandar, media


def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2+y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_de_agujas #A mayor cantidad de agujas el cálculo del área es más preciso.


def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, agujas={numero_de_agujas}')

    return (media_estimados, sigma)


def estimar_pi(precision, numero_de_intentos):
    """Aumenta el número de agujas para conseguir una diminución entre la variación de 
    los valores de pi disminuyendo así la variación estándar para conseguir que dentro 
    del porcentaje de confianza de 95% (1.96) no varíe más allá de la precisión indicada (0.01).
    """
    numero_de_agujas = 1000
    sigma = precision

    while 1.96 * sigma >= precision: #Precisión es el valor de la(s) desviación(es) estándar que se necesita. En este caso es para 1.96 desv. std.
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2 #Al aumentar el número de agujas los valores de PI se encontrarán más cerca de la media, disminuyendo la desviación estándar, aumentando la exactitud del cálculo

    return media


if __name__ == "__main__":
    estimar_pi(0.01, 1000)

