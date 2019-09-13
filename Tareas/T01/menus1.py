from parametros import PATHS, DINERO_INI, EQUIPOS, \
    BICICLETA, MOTOCICLETA, AUTOMOVIL, TRONCOMOVIL
from pilotos import Piloto
from collections import defaultdict
from random import randint, sample
from abstracts import Menu
from vehiculos import Troncomovil, Motocicleta, Bicicleta, Automovil
import menus2

class MenuSesion(Menu):
    def __init__(self):
        super().__init__()
        self.principal = menus2.MenuPrincipal()
        

    def crear_vehiculo(self, dueno):
        nom_vehiculo = input('Por favor indique el nombre de su vehiculo inicial:  ')
        nombre = nom_vehiculo.replace(' ', '')
        if not nombre.isalnum():
            print('Nombre del vehiculo no valido.')
            return self.crear_vehiculo()
        
        else:
            existe = 0
            with open(PATHS['VEHICULOS'], 'r', encoding='utf-8') as archivo:
                # Se genera un molde para buscar en que posicion 
                # se encuentra le nombre de los pilotos
                molde = archivo.readline()
                molde = molde.strip().split(',')
                for m in molde:
                    if m == 'Nombre':
                        nom = molde.index(m)
                for l in archivo:
                    vehiculo = l.strip().split(',')
                    if vehiculo[nom] == nom_vehiculo:
                        existe = 1

            if existe == 1:
                print('Nombre del vehiculo ya existe.')
                vehiculo = self.crear_vehiculo()
                return vehiculo

            else:
                tipo = input('Por favor indique el tipo de vehiculo que desea:  ')
                tipo_mayus = tipo.upper()
                print(tipo_mayus)
                if not tipo_mayus in ['TRONCOMOVIL', 'BICICLETA', 
                    'MOTOCICLETA','AUTOMOVIL']:
                    print('Tipo de vehiculo invalido')
                    vehiculo = self.crear_vehiculo()
                    return vehiculo 
                else:
                    if tipo_mayus == 'TRONCOMOVIL':
                        
                        vehiculo = Troncomovil()

                        return vehiculo
                    elif tipo_mayus == 'MOTOCICLETA':
                        vehiculo = Motocicleta()
                        return vehiculo

                    elif tipo_mayus == 'BICICLETA':
                        vehiculo = Bicicleta()
                        return vehiculo
                    else:
                        vehiculo = Automovil()
                        return vehiculo


    def crear_piloto(self):
        nom_usuario = input('Por favor indique su nombre de piloto:    ')
        nombre = nom_usuario.replace(' ', '')
        if not nombre.isalnum():
            print('Nombre de piloto no valido.')
            self.crear_partida()

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
                    piloto = l.strip().split(',')
                    if piloto[nom] == nom_usuario:
                        existe = 1

            if existe == 1:
                print('Nombre de piloto ya existe.')
                self.crear_partida()
            else:
                equipo = input('Por favor indique el equipo al cual prefiere pertenecer \
(Tareos, Hibridos o Docencios ):  ')
                exp = 0
                equi = equipo.upper()

                if not equi in ['TAREOS', 'HIBRIDOS', 'DOCENCIOS']:
                    print('Nombre de equipo invalido, vuelva a empezar.')
                    self.crear_partida()

                else:
                    contextura = randint(EQUIPOS[equi]['CONTEXTURA']['MIN'], 
                        EQUIPOS[equi]['CONTEXTURA']['MAX'])
                    equilibrio = randint(EQUIPOS[equi]['EQUILIBRIO']['MIN'], 
                        EQUIPOS[equi]['EQUILIBRIO']['MAX'])
                    if equi == 'HIBRIDOS':
                        personalidad = sample(EQUIPOS[equi]['PERSONALIDAD'], 1)[0]
                    
                    else:
                        personalidad = EQUIPOS[equi]['PERSONALIDAD']
                    
                    dinero = DINERO_INI
                    piloto_nuevo = Piloto(nom_usuario, 
                            dinero, personalidad, contextura, 
                            equilibrio, exp, equipo)
                    print(piloto_nuevo)
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
            linea = '\n'
            for l in lista:
                
                linea += str(l)
                if l == lista[len(lista)-1]:
                    pass
                else:
                    linea += ','
            print(linea)
            archivo.write(linea)


        vehiculo = self.crear_vehiculo(piloto._nombre)
        self.ir_menu(piloto, vehiculo)
    
    def ir_menu(piloto, vehiculo):
        from menus2 import MenuPrincipal
        menu = MenuPrincipal(piloto, vehiculo)
        menu.menu()
 
    def cargar_partida(self):
        from menus2 import MenuPrincipal
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
            self.cargar_partida()
        elif inpt == '0':
            self.salir()
        else:
            print('Respuesta invalida, por favor indique nuevamente.')
            self.menu()
        



