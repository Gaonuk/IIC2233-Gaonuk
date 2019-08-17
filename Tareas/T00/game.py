# Modulos importados 
import tablero 
import parametros
import os 
import random 
import math
import sys

#Variables globales
baldosasVacias = 0
baldDesc = 0
puntaje = 0
letras = 'ABCDEFGHIJKLMNO'
usuario = ''
numLegos = 0


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
    global numLegos
    global baldosasVacias
    global usuario
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
        
        # Se crean dos tableros distintos, uno contiene la posicion de los Legos 
        # y el otro es el tablero que se le muestra al usuario

        tablaUsuario = crearTablero(int(n) , int(m))
        tabla = crearTablero(int(n), int(m))
        
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


        tablero.print_tablero(tabla)
        printJuego(tablaUsuario, tabla)


    elif resp == '2':
        return 2
    elif resp == '3':
        return 3
    else:
        resp = input('Respuesta invalida! Por favor indique una nueva opcion: ')
        menuPrincipal(resp)


def printJuego(tablaUsuario, mainTabla):
    tablero.print_tablero(tablaUsuario)
    print('Seleccione una de las siguientes acciones:')
    print(' [1] Descubrir una baldosa')
    print(' [2] Guardar la partida')
    print(' [0] Salir de la partida')
    opcion = input('Indique su opcion (0, 1 o 2):  ')
    if opcion.isdigit():
        mainJuego(tablaUsuario, opcion, mainTabla)
    else:
        print('Respuesta Invalida!')
        printJuego(tablaUsuario, mainTabla)


def mainJuego(tablaUsuario, opcion, mainTabla):
    global baldosasVacias
    global letras
    global baldDesc
    if opcion == '1':
        print('Por favor indique las coordenadas de la baldosa que desea descubrir:')
        c1 = input('Coordenada 1 (numeros): ')
        c2 = input('Coordenada 2 (letras): ')
        if not c1.isdigit() or not c2.isalpha():
            print('Coordenadas invalidas.')
            mainJuego(tablaUsuario, '1', mainTabla)
        elif int(c1) >= len(tablaUsuario):
            print('Coordenada fuera del rango valido')
            mainJuego(tablaUsuario, '1', mainTabla)
        elif ord(c2) < ord('A') or ord(c2) > ord(letras[len(tablaUsuario)-1]):
            print('Coordenada fuera del rango valido')
            mainJuego(tablaUsuario, '1', mainTabla)

        else:
           
            c1 = int(c1)
            for l, i in enumerate(letras):
                if i == c2:
                    c3 = l
                    break
            minasAledanas = 0

            if mainTabla[c1][c3] == 'L':
                gameOver(mainTabla)

            elif c1 == 0:
                if c3 == 0:
                    if mainTabla[c1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3 + 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)
                elif c3 == len(mainTabla[0])-1 :
                    if mainTabla[c1][c3 - 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3 - 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)
                else:
                    if mainTabla[c1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1][c3 - 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 + 1][c3 - 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)
            elif c1 == len(mainTabla)-1:
                if c3 == 0:
                    if mainTabla[c1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3 + 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)
                elif c3 == len(mainTabla[0])-1 :
                    if mainTabla[c1][c3 - 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3 - 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)
                else:
                    if mainTabla[c1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1][c3 - 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3 + 1] == 'L':
                        minasAledanas += 1
                    if mainTabla[c1 - 1][c3 - 1] == 'L':
                        minasAledanas += 1
                    tablaUsuario[c1][c3] = minasAledanas
                    baldDesc += 1
                    printJuego(tablaUsuario, mainTabla)


            
                
    elif opcion == '2':
        pass
    else:
        pass


def gameOver(tabla):                   
    global usuario 
    global puntaje 
    global baldDesc
    global numLegos
    print('Te has topado con un Lego! Perdiste la partida ' + usuario + '!')
    tablero.print_tablero(tabla)
    puntaje = numLegos * baldDesc * parametros.POND_PUNT
    print('Puntaje final : ' + str(puntaje))
    rank = open('puntajes.txt', 'a')


if __name__ == "__main__":
    opcion = printMenu()
    menuPrincipal(opcion)

        