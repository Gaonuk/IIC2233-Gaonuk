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


# Funcion que crea el tablero del juego en funcion de los 
# datos introducidos por el usuario 
def crearTablero(n, m):
    largo = [[' ' for x in range(m)] for x in range(n)]
    return largo


# Funcion que imprime el menu principal del juego 
def printMenu():
    print('*******************************************************')
    print('               BIENVENIDO A LEGOSWEEPER!               ')
    print('*******************************************************\n')
    print(' Seleccione una opcion:  \n')
    print('     [1] Crear partida   \n')
    print('     [2] Cargar partida  \n')
    print('     [3] Ver ranking     \n')
    print('     [0] Salir           \n')
    resp = input('Indique su resp (0, 1, 2 o 3):  ')
    menuPrincipal(resp) 


# Funcion que habilita el menu principal 
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
                print('Valor fuera del rango establecido\n')
                menuPrincipal('1')
        else:
            print('Respuesta Invalida.\n')
            menuPrincipal('1')
        m = input('Por favor, introduzca el ancho del tablero:  ')
        if m.isdigit():
            if int(m) <= 15 and int(m) >= 3:
                pass
            else:
                print('Valor fuera del rango establecido\n')
                menuPrincipal('1')
        else:
            print('Respuesta Invalida.\n')
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
        checkPuntajes()
    else:
        resp = input('Respuesta invalida! Por favor indique una nueva opcion: \n')
        menuPrincipal(resp)


def printJuego(tablaUsuario, mainTabla):
    global baldosasVacias
    global baldDesc

    if baldDesc == baldosasVacias:
        victoria()
    else:
        tablero.print_tablero(tablaUsuario)
        print('Seleccione una de las siguientes acciones:\n')
        print(' [1] Descubrir una baldosa\n')
        print(' [2] Guardar la partida\n')
        print(' [0] Salir de la partida\n')
        opcion = input('Indique su opcion (0, 1 o 2):  ')
        if opcion.isdigit():
            mainJuego(tablaUsuario, opcion, mainTabla)
        else:
            print('Respuesta Invalida!\n')
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
            print('Coordenadas invalidas.\n')
            mainJuego(tablaUsuario, '1', mainTabla)
        elif int(c1) >= len(tablaUsuario):
            print('Coordenada fuera del rango valido\n')
            mainJuego(tablaUsuario, '1', mainTabla)
        elif ord(c2) < ord('A') or ord(c2) > ord(letras[len(tablaUsuario)-1]):
            print('Coordenada fuera del rango valido\n')
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

            elif tablaUsuario[c1][c3] != ' ':
                print('Ya has descubierto esta baldosa!\n')
                printJuego(tablaUsuario, mainTabla)


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
            elif c3 == 0:
                if mainTabla[c1][c3 + 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3 + 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3 + 1] == 'L':
                    minasAledanas += 1
                tablaUsuario[c1][c3] = minasAledanas
                baldDesc += 1
                printJuego(tablaUsuario, mainTabla)
            elif c3 == len(mainTabla[0])-1:
                if mainTabla[c1][c3 - 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3 - 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3 - 1] == 'L':
                    minasAledanas += 1
                tablaUsuario[c1][c3] = minasAledanas
                baldDesc += 1
                printJuego(tablaUsuario, mainTabla)
            else:
                if mainTabla[c1][c3 - 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1][c3 + 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3 - 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 - 1][c3 + 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3 - 1] == 'L':
                    minasAledanas += 1
                if mainTabla[c1 + 1][c3 + 1] == 'L':
                    minasAledanas += 1
                tablaUsuario[c1][c3] = minasAledanas
                baldDesc += 1
                printJuego(tablaUsuario, mainTabla)

            
                
    elif opcion == '2':
        pass
    elif opcion == '0':
        printMenu()
    else:
        print('Respuesta invalida.')
        printJuego(tablaUsuario, mainTabla)


def victoria():
    global usuario
    global puntaje
    global baldosasVacias
    global numLegos
    print('Has descubierto todas las baldosas vacias! Felicidades ' + usuario + ' has ganado!')
    puntaje = numLegos * baldosasVacias * parametros.POND_PUNT
    print('Puntaje final: ' + str(puntaje))
    rank = open('puntajes.txt', 'a')
    partida = usuario + ',' + ' ' + 'Puntaje:' + ' ' + str(puntaje) + ' \n'
    rank.write(partida)


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
    partida = usuario + ',' + ' ' + 'Puntaje:' + ' ' + str(puntaje) + ' \n'
    rank.write(partida) 

def checkPuntajes():
    listado = open('puntajes.txt', 'r')
    listPuntajes = []

    for l in listado:
        listPuntajes.append(l.split(' '))

    if len(listPuntajes) == 0:
        print('Aun no hay puntajes en el ranking! Comienza una partida!')
    
    else:
        listPuntajes.sort(reverse=True, key=lambda x: int(x[2]))
        n = 1
        print('Los diez mejores puntajes son:\n ')
        if len(listPuntajes) >= 10:
            i = 0
            while i < 10:
                rank = str(n) + ':' + ' ' + listPuntajes[i][0] + ' ' + listPuntajes[i][1] + ' ' + listPuntajes[i][2] + '\n'
                print(rank)
                n += 1
                i += 1
        else:
            for i in listPuntajes:
                rank = str(n) + ':' + ' ' + i[0] + ' ' + i[1] + ' ' + i[2] + '\n'
                print(rank)
                n += 1
        
        

    

if __name__ == "__main__":
    printMenu()


        