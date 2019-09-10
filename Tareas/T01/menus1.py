from parametros import PATHS, DINERO_INI
from pilotos import Piloto
from collections import defaultdict
from random import randint, sample
from menus2 import *
from menus3 import Menu
    
class MenuSesion(Menu):
    def __init__(self):
        super().__init__()
        

    def crear_piloto(self):
        nom_usuario = input('Por favor indique su nombre de piloto:    ')
        nombre = nom_usuario.replace(' ', '')
        if not nombre.isalnum():
            print('Nombre de piloto no valido.')
            self.crear_piloto()

        else:
            existe = 0
            with open(PATHS['PILOTOS'], 'r', encoding='utf-8') as archivo:
                # Se genera un molde para buscar en que posicion 
                # se encuentra le nombre de los pilotos
                molde = archivo.readline()
                molde = molde.strip().split(',')
                for m in molde:
                    if m == 'Nombre':
                        nom = molde.index(m)
                for l in archivo:
                    piloto = l.split(',')
                    if piloto[nom] == nom_usuario:
                        existe = 1

            if existe == 1:
                print('Nombre de piloto ya existe.')
                self.crear_piloto()
            else:
                equipo = input('Por favor indique el equipo al cual prefiere pertenecer:    ')
                exp = 0

                if equipo.lower() == 'tareos':
                    contextura = randint(26, 45)
                    equilibro = randint(36, 55)
                    personalidad = 'precavido'
                    dinero = DINERO_INI
                    piloto_nuevo = Piloto(nom_usuario, 
                        dinero, personalidad, contextura, 
                        equilibro, exp, equipo)
                    return piloto_nuevo

                elif equipo.lower() == 'hibridos' \
                    or equipo.lower() == 'híbridos': 
                    contextura = randint(35, 54)
                    equilibro = randint(20, 34)
                    lista = ['precavido', 'osado']
                    personalidad = sample(lista, 1)[0]
                    dinero = DINERO_INI
                    piloto_nuevo = Piloto(nom_usuario, 
                        dinero, personalidad, contextura, 
                        equilibro, exp, equipo)
                    return piloto_nuevo

                elif equipo.lower() == 'docencios':
                    contextura = randint(44, 60)
                    equilibro = randint(4, 10)
                    personalidad = 'osado'
                    piloto_nuevo = Piloto(nom_usuario, 
                        dinero, personalidad, contextura, 
                        equilibro, exp, equipo)
                    return piloto_nuevo


    def crear_partida(self):
        piloto = self.crear_piloto()
        lista = ['']*7
        orden = defaultdict(int)
        with open(PATHS['PILOTOS'], 'r+', encoding='utf-8') as archivo:
            molde = archivo.readline()
            molde = molde.strip().split(',')
            for m in molde:
                orden[m] = molde.index(m)
            lista[orden['Nombre']] = piloto._nombre
            lista[orden['Dinero']] = piloto.saldo            
            lista[orden['Personalidad']] = piloto._personalidad            
            lista[orden['Contextura']] = piloto.contextura            
            lista[orden['Equilibrio']] = piloto._equilibrio            
            lista[orden['Experiencia']] = piloto.experiencia
            lista[orden['Equipo']] = piloto._equipo
            linea = ''
            for l in lista:
                
                linea += str(l)
                if l == lista[len(lista)-1]:
                    linea += '\n'
                else:
                    linea += ','

            archivo.write(linea)



        # menu = MenuPrincipal(piloto)
        # menu.menu()
    
    def cargar_partida(self):
        piloto = self.cargar_piloto()
        menu = MenuPrincipal(piloto)
        menu.menu()



    def cargar_piloto(self):
        orden = defaultdict(int)
        nombre = input('Por favor introduzca su nombre de piloto:   ')
        with open(PATHS['PILOTOS'], 'r', encoding='utf-8') as archivo:
            molde = archivo.readline()
            molde = molde.strip().split(',')
            for m in molde:
                orden[m] = molde.index(m)
            for l in archivo:
                piloto = l.strip().split(',')
                print(piloto)
                if nombre == piloto[orden['Nombre']]:
                    piloto_cargado = Piloto(
                        piloto[orden['Nombre']], 
                        piloto[orden['Dinero']],
                        piloto[orden['Personalidad']], 
                        piloto[orden['Contextura']], 
                        piloto[orden['Equilibro']], 
                        piloto[orden['Experiencia']], 
                        piloto[orden['Equipo']]
                        )
                    
                    return piloto_cargado
            
            print('No existe un piloto con ese nombre, por favor cree \
                una nueva partida.')
            

    def salir(self):
        print('Se ha cerrado el juego exitosamente.')


    def menu(self):
        print(self._menu)

        print('[1] - Crear una nueva partida')
        print('[2] - Cargar una partida')
        print('[0] - Salir del juego')

        inpt = self.recibir_input()

        if inpt == '1':
            self.crear_partida()
        elif inpt == '2':
            piloto = self.cargar_partida()
            menu = MenuPrincipal(piloto)
            menu.menu()
        elif inpt == '0':
            self.salir()
        else:
            print('Respuesta invalida, por favor indique nuevamente.')
            self.menu()
        



