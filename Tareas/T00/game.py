# Modulos importados 
import tablero 
import parametros
import os 
import random 
import math


def crearTablero(n, m):
    largo = [[' ' for x in range(m)] for x in range(n)]
    return largo


def printMenu():
    print('*******************************************************')
    print('            BIENVENIDO A LEGOSWEEPER!                  ')
    print('*******************************************************')
    print(' Seleccione una opcion:')
    print('     [1] Crear partida')
    print('     [2] Cargar partida')
    print('     [3] Ver ranking')
    print('     [0] Salir')
    resp = input('Indique su resp (0, 1, 2 o 3):  ')
    return resp 

    
def menuPrincipal(resp):
    if resp == '0':
        return 
    elif resp == '1':
        n = input('Por favor, introduzca el largo del tablero:  ')
        if n.isdigit():
            if int(n) <= 15 and int(n) >= 3:
                print('wena')
            else:
                print('Valor fuera del rango establecido')
                menuPrincipal('1')
        else:
            print('Respuesta Invalida.')
            menuPrincipal('1')
        m = input('Por favor, introduzca el ancho del tablero:  ')
        if m.isdigit():
            if int(m) <= 15 and int(m) >= 3:
                print('wena')
            else:
                print('Valor fuera del rango establecido')
                menuPrincipal('1')
        else:
            print('Respuesta Invalida.')
            menuPrincipal('1')
        usuario = input('Por favor, introduzca su nombre de usuario:  ')
        
        tabla = crearTablero(int(n) , int(m))
        
        # tablero.print_tablero(tabla)
        
        numLegos = math.ceil(int(n) * int(m) * parametros.PROB_LEGO)
        i = 0
        while i < numLegos:
            n1 = random.randrange(len(tabla))
            n2 = random.randrange(len(tabla[0]))
            if tabla[n1][n2] != 'L':
                tabla[n1][n2] = 'L'
                i += 1
            else:
                pass
        
        printJuego(tabla)

    elif resp == '2':
        return 2
    elif resp == '3':
        return 3
    else:
        resp = input('Respuesta invalida! Por favor indique una nueva opcion: ')
        menuPrincipal(resp)


def printJuego(tabla):
    tablero.print_tablero(tabla)
    print('Seleccione una de las siguientes acciones:')
    print(' [1] Descubrir una baldosa')
    print(' [2] Guardar la partida')
    print(' [0] Salir de la partida')
    opcion = input('Indique su opcion (0, 1 o 2):  ')
    if opcion.isdigit():
        mainJuego(tabla, opcion)
    else:
        print('Respuesta Invalida!')
        printJuego(tabla)


def mainJuego(tabla, opcion):
    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    else:
        pass


if __name__ == "__main__":
    opcion = printMenu()
    menuPrincipal(opcion)

        