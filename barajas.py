import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas        


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def obtener_pares(manos):
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for cantidad in counter.values():
            if cantidad == 2:
                pares += 1
                break #termina porque se encontró 1 par que es lo que buscábamos

    return pares


def obtener_corridas(manos):
    corridas = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        
        mano_corrida = []
        for valor_carta, cantidad in counter.items():    
            if cantidad > 1:
                break #No puede haber un VALOR de carta con más de una carta en la mano.
            elif cantidad == 1:
                mano_corrida.append(valor_carta) 

        if len(mano_corrida) == tamano_mano: #Verifica que la mano donde puede estar la corrida (mano_corrida) se haya completado con 5 cartas únicas           
            mano_corrida.sort() #ordena las cartas únicas de la corrida para comprobar si es corrida

            es_corrida = True
            for i in range(len(mano_corrida) - 1): #recorre la mano para verificar si cada carta siguiente es mayor por 1 a la anterior. De serlo en todas las cartas será corrida
                if mano_corrida[i] != mano_corrida[i+1] - 1:
                    es_corrida = False
                    break            
            if es_corrida:
                corridas += 1

    return corridas


def main(tamano_mano, intentos, opcion):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    if opcion == 'a':
        pares = obtener_pares(manos)

        probabilidad_par = pares / intentos    
        print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es de {probabilidad_par}')

    elif opcion == 'b':
        corridas = obtener_corridas(manos) 
        probabilidad_corrida = corridas / intentos
        print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} cartas es de {probabilidad_corrida}')



if __name__ == "__main__":
    tamano_mano = int(input('¿De cuántas cartas será la mano? '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad? '))
    opcion = input("""¿Probabilidad de qué te gustaría obtener?
    A) Obtener un par
    B) Obtener una corrida
    """)
    opcion = opcion.lower()
    
    main(tamano_mano, intentos, opcion)