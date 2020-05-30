import random
import collections

def sacar_bola(bolas, numero_de_bolas_a_extraer):
    secuencia_de_bolas = random.sample(bolas, numero_de_bolas_a_extraer)
    # print(secuencia_de_bolas)

    return secuencia_de_bolas
    

def main(numero_bolas_rojas, numero_bolas_blancas, numero_de_bolas_a_extraer, numero_de_intentos):
    bolas = []
    for _ in range(numero_bolas_rojas):
        bolas.append('roja')

    for _ in range(numero_bolas_blancas):
        bolas.append('blanca')

    print(f'Bolas en la bolsa: {bolas}')

    bolas_extraidas = []
    for _ in range(numero_de_intentos):
        secuencia_de_bolas = sacar_bola(bolas, numero_de_bolas_a_extraer)
        bolas_extraidas.append(secuencia_de_bolas) #lista de todas las bolas por cada intento separadas como listas dentro de una lista 

    bolas_rojas = 0
    bolas_blancas = 0
    for bolas in bolas_extraidas: #bolas es una lista de n bolas
        counter = dict(collections.Counter(bolas))
        # print(counter)
        for color, cantidad in counter.items():
            if color == 'roja' and cantidad == 2:
                bolas_rojas += 1  
            if color == 'blanca' and cantidad == 2:
                bolas_blancas += 1  
            
    probabilidad_dos_bolas_rojas = bolas_rojas / numero_de_intentos
    print(f'Probabilidad de extraer dos bolas rojas: {probabilidad_dos_bolas_rojas}')

    probabilidad_dos_bolas_blancas = bolas_blancas / numero_de_intentos
    print(f'Probabilidad de extraer dos bolas blancas: {probabilidad_dos_bolas_blancas}')


if __name__ == "__main__":
    numero_bolas_rojas = int(input('¿Cuántas bolas rojas? '))
    numero_bolas_blancas = int(input('¿Cuántas bolas blancas? '))
    numero_de_bolas_a_extraer = int(input('¿Cuántas bolas extraerás? '))
    numero_de_intentos = int(input('¿Cuántas veces correrás la simulación? '))

    main(numero_bolas_rojas, numero_bolas_blancas, numero_de_bolas_a_extraer, numero_de_intentos)