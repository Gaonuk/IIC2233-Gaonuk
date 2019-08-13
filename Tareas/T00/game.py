# Modulos importados 
import tablero
import parametros
import os 
import random 
import math


def crearTablero(n, m):
    ancho = []
    for l in range(m):
        ancho.append(' ')
    tablero = []
    for a in range(n):
        tablero.append(ancho)
    return tablero

def printMenu():
    print('Seleccione una opcion:')
    print('[1] Crear partida')
    print('[2] Cargar partida')
    print('[3] Ver ranking')
    print('[0] Salir')
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
        
        tablero.print_tablero(tabla)
        
        numLegos = math.ceil(int(n) * int(m) * parametros.PROB_LEGO)
        print(numLegos)
        for k in range(numLegos):
            num1 = random.randint(0, int(n) - 1)
            num2 = random.randint(0, int(m) - 1)
            tabla[num1][num2] = 'L'

        tablero.print_tablero(tabla)

    elif resp == '2':
        return 2
    elif resp == '3':
        return 3
    else:
        resp = input('Respuesta invalida! Por favor indique una nueva opcion: ')
        menuPrincipal(resp)


def menuJuego():
    print('')


if __name__ == "__main__":
    opcion = printMenu()
    menuPrincipal(opcion)

        