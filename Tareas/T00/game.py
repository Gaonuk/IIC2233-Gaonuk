# Modulos importados 
import tablero 
import parametros
import os 
import random 
import math
import sys
baldosasVacias = 0
letras = 'ABCDEFGHIJKLMNO'

def crearTablero(n, m):
    largo = [[' ' for x in range(m)] for x in range(n)]
    return largo


def printMenu():
    print('*******************************************************')
    print('               BIENVENIDO A LEGOSWEEPER!               ')
    print('*******************************************************')
    print(' Seleccione una opcion:  ')
    print('     [1] Crear partida   ')
    print('     [2] Cargar partida  ')
    print('     [3] Ver ranking     ')
    print('     [0] Salir           ')
    resp = input('Indique su resp (0, 1, 2 o 3):  ')
    return resp 

    
def menuPrincipal(resp):
    global baldosasVacias
    if resp == '0':
        return 
    elif resp == '1':
        n = input('Por favor, introduzca el largo del tablero:  ')
        if n.isdigit():
            if int(n) <= 15 and int(n) >= 3:
                pass
            else:
                print('Valor fuera del rango establecido')
                menuPrincipal('1')
        else:
            print('Respuesta Invalida.')
            menuPrincipal('1')
        m = input('Por favor, introduzca el ancho del tablero:  ')
        if m.isdigit():
            if int(m) <= 15 and int(m) >= 3:
                pass
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
        

        for n in tabla:
            for k in n:
                if k != 'L':
                    baldosasVacias += 1

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
    print(tabla)
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
    global baldosasVacias
    global letras
    if opcion == '1':
        print('Por favor indique las coordenadas de la baldosa que desea descubrir:')
        c1 = input('Coordenada 1 (numeros): ')
        c2 = input('Coordenada 2 (letras): ')
        if not c1.isdigit() or not c2.isalpha():
            print('Coordenadas invalidas.')
            mainJuego(tabla, '1')
        elif int(c1) >= len(tabla):
            print('Coordenada fuera del rango valido')
            mainJuego(tabla, '1')
        elif ord(c2) < ord('A') or ord(c2) > ord(letras[len(tabla)-1]):
            print('Coordenada fuera del rango valido')
            mainJuego(tabla, '1')

        else:
            print(baldosasVacias)
            c1 = int(c1)
            for l, i in enumerate(letras):
                if i == c2:
                    c3 = l
                    break
            minasAledanas = 0

            # if c1 == 0:
            #     if c3 == 0:
            if tabla[c1][c3] == 'L':
                minasAledanas += 1
            if tabla[c1][c3 + 1] == 'L':
                minasAledanas += 1
            if tabla[c1 + 1][c3] == 'L':
                minasAledanas += 1
            if tabla[c1 + 1][c3 + 1] == 'L':
                minasAledanas += 1
            tabla[c1][c3] = minasAledanas

            printJuego(tabla)
                
    elif opcion == '2':
        pass
    else:
        pass


if __name__ == "__main__":
    opcion = printMenu()
    menuPrincipal(opcion)

        