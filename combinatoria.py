import sys

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def variaciones_sin_repeticion(m, n):
    return factorial(m) / factorial(m - n)


def variaciones_con_repeticion(m, n):
    return m**n


def permutaciones_sin_repeticion(m):
    return factorial(m)


def permutaciones_con_repeticion(m):
    elementos_unicos = int(input('¿Cuántos elementos únicos hay en la muestra? '))

    cantidad_elementos_unicos = []
    for i in range(elementos_unicos):
        cantidad = int(input(f'¿Cuántos datos hay del elemento {i + 1}? '))
        cantidad_elementos_unicos.append(cantidad)

    total_cantidades = 0
    for cantidad in cantidad_elementos_unicos:
        total_cantidades += cantidad
    
    if total_cantidades == m:
        denominador = 1
        for cantidad in cantidad_elementos_unicos: #Calculando el producto de los factoriales de las cantidades de cada elemento único
            denominador *= factorial(cantidad)
        
        return permutaciones_sin_repeticion(m) / denominador

    else:
        print(f'El total de cantidades de los elementos únicos {total_cantidades} coincide con el tamaño de la muestra de elementos m = {m}')
        print('Intenta de nuevo, por favor')


def combinaciones_sin_repeticion(m, n):
    # return variaciones_sin_repeticion(m, n) / permutaciones_sin_repeticion(n)    

    return factorial(m) / (factorial(n) * factorial(m - n)) #Formula con factoriales


def combinaciones_con_repeticion(m, n):
    return factorial(m + n - 1) / (factorial(n) * factorial(m - 1))


def main(opcion):
    total_de_elementos = int(input('¿Cuál es el tamaño de tu muestra de elementos? '))

    if opcion == 'a':
        tamano_variaciones = int(input('¿De qué tamaño serán las variaciones? '))
        variaciones = variaciones_sin_repeticion(total_de_elementos, tamano_variaciones)
        print(f'Variaciones sin repetición = {variaciones}')
    
    elif opcion == 'b':
        tamano_variaciones = int(input('¿De qué tamaño serán las variaciones? '))
        variaciones = variaciones_con_repeticion(total_de_elementos, tamano_variaciones)
        print(f'Variaciones con repetición = {variaciones}')
        
    elif opcion == 'c':
        permutaciones = permutaciones_sin_repeticion(total_de_elementos)
        print(f'Permutaciones sin repetición = {permutaciones}')

    elif opcion == 'd':
        permutaciones = permutaciones_con_repeticion(total_de_elementos)
        print(f'Permutaciones con repetición = {permutaciones}')

    elif opcion == 'e':
        tamano_combinaciones = int(input('¿De qué tamaño serán las combinaciones? '))
        combinaciones = combinaciones_sin_repeticion(total_de_elementos, tamano_combinaciones)
        print(f'Combinaciones sin repetición = {combinaciones}')

    elif opcion == 'f':
        tamano_combinaciones = int(input('¿De qué tamaño serán las combinaciones? '))
        combinaciones = combinaciones_con_repeticion(total_de_elementos, tamano_combinaciones)
        print(f'Combinaciones con repetición = {combinaciones}')

    elif opcion == 'g':
        factorial_calculado = factorial(total_de_elementos)
        print(f'Factorial = {factorial_calculado}')

        

if __name__ == "__main__":
    sys.setrecursionlimit(100002)
    opcion = input("""¿Qué desdeas calcular? 
    a) Variaciones sin repetición
    b) Variaciones con repetición
    c) Permutaciones sin repetición
    d) Permutaciones con repetición
    e) Combinaciones sin repetición
    f) Combinaciones con repetición
    g) Factorial
    """)

    opcion = opcion.lower()
    
    main(opcion)