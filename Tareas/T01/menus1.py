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
                tipo = input('Por favor indique el tipo de vehiculo \
que desea (no ingrese acentos):  ')
                tipo_mayus = tipo.upper()
                if not tipo_mayus in ['TRONCOMOVIL', 'BICICLETA', 
                    'MOTOCICLETA','AUTOMOVIL']:
                    print('Tipo de vehiculo invalido')
                    vehiculo = self.crear_vehiculo()
                    return vehiculo 
                else:
                    if tipo_mayus == 'TRONCOMOVIL':

                        chasis = randint(TRONCOMOVIL['CHASIS']['MIN'], 
                            TRONCOMOVIL['CHASIS']['MAX'])

                        carroceria = randint(TRONCOMOVIL['CARROCERIA']['MIN'],
                            TRONCOMOVIL['CARROCERIA']['MAX'])

                        ruedas = randint(TRONCOMOVIL['RUEDAS']['MIN'],
                            TRONCOMOVIL['RUEDAS']['MAX'])

                        zapatillas = randint(TRONCOMOVIL['ZAPATILLAS']['MIN'],
                            TRONCOMOVIL['ZAPATILLAS']['MAX'])

                        peso = randint(TRONCOMOVIL['PESO']['MIN'],
                            TRONCOMOVIL['PESO']['MAX'])

                        vehiculo = Troncomovil(nom_vehiculo, dueno, 
                            chasis, carroceria, ruedas, zapatillas, peso)
                        return vehiculo

                    elif tipo_mayus == 'MOTOCICLETA':

                        chasis = randint(MOTOCICLETA['CARROCERIA']['MIN'],
                            MOTOCICLETA['CARROCERIA']['MAX'])

                        carroceria = randint(MOTOCICLETA['CARROCERIA']['MIN'],
                            MOTOCICLETA['CARROCERIA']['MAX'])

                        ruedas = randint(MOTOCICLETA['RUEDAS']['MIN'],
                            MOTOCICLETA['RUEDAS']['MAX'])

                        motor = randint(MOTOCICLETA['MOTOR']['MIN'],
                            MOTOCICLETA['MOTOR']['MAX'])

                        peso = randint(MOTOCICLETA['PESO']['MIN'],
                            MOTOCICLETA['PESO']['MAX'])

                        vehiculo = Motocicleta(nom_vehiculo, dueno, 
                            chasis, carroceria, ruedas, motor, peso)
                        return vehiculo

                    elif tipo_mayus == 'BICICLETA':
                        
                        chasis = randint(BICICLETA['CHASIS']['MIN'], 
                            BICICLETA['CHASIS']['MAX'])

                        carroceria = randint(BICICLETA['CARROCERIA']['MIN'],
                            BICICLETA['CARROCERIA']['MAX'])

                        ruedas = randint(BICICLETA['RUEDAS']['MIN'],
                            BICICLETA['RUEDAS']['MAX'])

                        zapatillas = randint(BICICLETA['ZAPATILLAS']['MIN'],
                            BICICLETA['ZAPATILLAS']['MAX'])

                        peso = randint(BICICLETA['PESO']['MIN'],
                            BICICLETA['PESO']['MAX'])

                        vehiculo = Bicicleta(nom_vehiculo, dueno, 
                            chasis, carroceria, ruedas, zapatillas, peso)
                        return vehiculo
                    else:

                        chasis = randint(AUTOMOVIL['CARROCERIA']['MIN'],
                            AUTOMOVIL['CARROCERIA']['MAX'])

                        carroceria = randint(AUTOMOVIL['CARROCERIA']['MIN'],
                            AUTOMOVIL['CARROCERIA']['MAX'])

                        ruedas = randint(AUTOMOVIL['RUEDAS']['MIN'],
                            AUTOMOVIL['RUEDAS']['MAX'])

                        motor = randint(AUTOMOVIL['MOTOR']['MIN'],
                            AUTOMOVIL['MOTOR']['MAX'])

                        peso = randint(AUTOMOVIL['PESO']['MIN'],
                            AUTOMOVIL['PESO']['MAX'])

                        vehiculo = Automovil(nom_vehiculo, dueno, 
                            chasis, carroceria, ruedas, motor, peso)
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
            lista[orden['Dinero']] = piloto.dinero            
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
            archivo.write(linea)


        vehiculo = self.crear_vehiculo(piloto._nombre)

        lista2 = ['']*8
        orden2 = defaultdict(int)
        with open(PATHS['VEHICULOS'], 'r+', encoding='utf-8') as archivo:
            molde = archivo.readline()
            molde = molde.strip().split(',')
            for m in molde:
                orden2[m] = molde.index(m)
            lista2[orden2['Nombre']] = vehiculo._nombre
            lista2[orden2['Dueño']] = vehiculo._dueno            
            lista2[orden2['Categoría']] = vehiculo.categoria            
            lista2[orden2['Chasis']] = vehiculo._chasis           
            lista2[orden2['Carrocería']] = vehiculo._carroceria            
            lista2[orden2['Ruedas']] = vehiculo._ruedas
            if vehiculo.categoria in ['bicicleta', 'troncomóvil']:
                lista2[orden2['Motor o Zapatillas']] = vehiculo._zapatillas
            else:
                lista2[orden2['Motor o Zapatillas']] = vehiculo._motor
            lista2[orden2['Peso']] = vehiculo._peso
            linea = '\n'
            for l in lista2:
                
                linea += str(l)
                if l == lista2[len(lista2)-1]:
                    pass
                else:
                    linea += ','
            archivo.write(linea)

        piloto.vehiculos.append(vehiculo)

        self.ir_menu(piloto)
    
    def ir_menu(self, piloto):
        menu = menus2.MenuPrincipal(piloto)
        menu.menu()
 
    def cargar_partida(self):
        piloto = self.cargar_piloto()
        self.ir_menu(piloto)



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
        



