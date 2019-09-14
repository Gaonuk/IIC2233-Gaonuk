import menus2
from parametros import PATHS
from collections import defaultdict
from pista import *
from abstracts import Menu
from pilotos import Contrincante

class MenuPreparacion(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
        self.pistas = []
    
    def cargar_pistas(self):
        orden = defaultdict(int)
        with open(PATHS['PISTAS'], 'r', encoding='utf-8') as archivo:
            molde = archivo.readline()
            molde = molde.strip().split(',')
            for m in molde:
                orden[m] = molde.index(m)
            for l in archivo:
                pista = l.strip().split(',')

                if pista[orden['Tipo']] == 'pista rocosa':
                    pista_cargando = PistaRocosa(
                        nombre=pista[orden['Nombre']], 
                        rocas=int(pista[orden['Rocas']]), 
                        dificultad=int(pista[orden['Dificultad']]), 
                        vueltas=int(pista[orden['NúmeroVueltas']]),  
                        contrincantes=pista[orden['Contrincantes']].split(';'),
                        largo=int(pista[orden['LargoPista']])
                    )
                    self.pistas.append(pista_cargando)
                
                elif pista[orden['Tipo']] == 'pista hielo':
                    pista_cargando = PistaHielo(
                        nombre=pista[orden['Nombre']], 
                        hielo=int(pista[orden['Hielo']]), 
                        dificultad=int(pista[orden['Dificultad']]), 
                        vueltas=int(pista[orden['NúmeroVueltas']]),  
                        contrincantes=pista[orden['Contrincantes']].split(';'),
                        largo=int(pista[orden['LargoPista']])
                    )
                    self.pistas.append(pista_cargando)

                else:
                    pista_cargando = PistaSuprema(
                        nombre=pista[orden['Nombre']], 
                        hielo=int(pista[orden['Hielo']]),
                        rocas=int(pista[orden['Rocas']]), 
                        dificultad=int(pista[orden['Dificultad']]), 
                        vueltas=int(pista[orden['NúmeroVueltas']]),  
                        contrincantes=pista[orden['Contrincantes']].split(';'),
                        largo=int(pista[orden['LargoPista']])
                    )
                    self.pistas.append(pista_cargando)
                

    def menu(self):
        self.cargar_pistas()
        print('Por favor seleccione la pista donde desea participar: ')
        lista_nombres = []
        for p in self.pistas:
            print(p.nombre)
            lista_nombres.append(p.nombre)

        inpt = self.recibir_input()
        if inpt == '0':
            self.volver_menu()

        elif not inpt in lista_nombres:
            print('Nombre de pista invalido, por favor intente nuevamente')
            self.menu()
        
        else:
            for p in self.pistas:
                if p.nombre == inpt:
                    pista_jugar = p

            print('Por favor indique el vehiculo que desea usar en la carrera')
            lista_vehiculos = []
            for v in self.piloto.vehiculos:
                print(v)
                lista_vehiculos.append(v.nombre)

            vehi_sel = self.recibir_input()

            if vehi_sel == '0':
                self.volver_menu()

            elif not vehi_sel in lista_vehiculos:
                print('No tiene ningun vehiculo con ese nombre')
                self.menu()
            else:
                for v in self.piloto.vehiculos:
                    if v.nombre == vehi_sel:
                        vehiculo_jugar = v
            

                self.ir_menu(self.piloto, vehiculo_jugar, pista_jugar)


    def ir_menu(self, piloto, vehiculo, pista):
        menu = MenuCarrera(piloto, vehiculo, pista)
        menu.menu()


            
    def volver_menu(self):
        menu = menus2.MenuPrincipal(self.piloto)
        menu.menu()



class MenuCarrera(Menu):
    def __init__(self, piloto, vehiculo, pista):
        super().__init__()
        self.piloto = piloto
        self.vehiculo = vehiculo
        self.pista = pista

    def ir_a_pits(self):
        pits = MenuPits(self.piloto, self.vehiculo, self.pista)
        pits.menu()


    def menu(self):
        while True:
            print()
            self.ir_a_pits()

class MenuPits(Menu):
    def __init__(self, piloto, vehiculo, pista):
        super().__init__()
        self.piloto = piloto
        self.pista = pista
        self.vehiculo = vehiculo

    def menu(self):
        print('Dinero disponible para reparaciones: {0}'.format(self.piloto.dinero))
        print('Partes a mejorar:')
        print('1) - Chasis             $100')
        print('2) - Carroceria         $50')
        print('3) - Ruedas             $120')
        print('4) - Zapatillas         $270')
    
        inpt = self.recibir_input()

        if inpt == '1':
            pass
        elif inpt == '2':
            pass
        elif inpt == '3':
            pass
        elif inpt == '4':
            pass
        elif inpt == '0':
            self.volver_carrera()

    def volver_carrera(self):
        pass

    def hacer_mejora(self):
        pass