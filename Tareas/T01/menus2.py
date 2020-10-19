from abstracts import Menu
import menus1
from collections import defaultdict
from parametros import PATHS, BICICLETA, \
    MOTOCICLETA, AUTOMOVIL, TRONCOMOVIL
from random import randint
from vehiculos import *
import menus3
class MenuPrincipal(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
    

    def iniciar_carrera(self):
        menu_carrera = menus3.MenuPreparacion(self.piloto)
        menu_carrera.menu()


    def comprar_vehiculos(self):
        menu_compras = MenuCompras(self.piloto)
        menu_compras.menu()


    def guardar_piloto(self):
        piloto = self.piloto
        lista = ['']*7
        orden = defaultdict(int)
        with open(PATHS['PILOTOS'], 'r+', encoding='utf-8') as archivo:
            lines = archivo.readlines()
            molde = lines[0]
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
            linea = ''
            for l in lista:
                linea += str(l)
                if l == lista[len(lista)-1]:
                    linea += ''
                else:
                    linea += ','
        with open(PATHS['PILOTOS'], 'w', encoding='utf-8') as archivo:
            for line in lines:
                if line.strip("\n").split(',')[orden['Nombre']] != piloto._nombre:
                    if line == lines[len(lines)-1]:
                        archivo.write(line.strip('\n'))
                    else:
                        archivo.write(line)
                else:
                    archivo.write(linea)


    def guardar_vehiculos(self, vehiculo):
        lista2 = ['']*8
        orden2 = defaultdict(int)
        with open(PATHS['VEHICULOS'], 'r+', encoding='utf-8') as archivo:
            lines = archivo.readlines()
            molde = lines[0]
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
            linea = ''
            for l in lista2:
                
                linea += str(l)
                if l == lista2[len(lista2)-1]:
                    linea += ''
                else:
                    linea += ','
            with open(PATHS['VEHICULOS'], 'w', encoding='utf-8') as archivo:
                existe = 0
                for line in lines:
                    if line.strip("\n").split(',')[orden2['Nombre']] != vehiculo._nombre:
                        if line == lines[len(lines)-1]:
                            archivo.write(line.strip('\n'))
                        else:
                            archivo.write(line)
                    else:
                        existe = 1
                        archivo.write(linea)

                if existe == 0:
                    archivo.write('\n')
                    archivo.write(linea)
    
    def guardar_partida(self):
        self.guardar_piloto()
        for vehiculo in self.piloto.vehiculos:
            self.guardar_vehiculos(vehiculo)
            

        

    def volver_menu(self):
        menu_sesion = menus1.MenuSesion()
        menu_sesion.menu()


    def menu(self):
        print(self._menu)

        print('[1] - Iniciar una carrera')
        print('[2] - Comprar nuevos vehiculos')
        print('[3] - Guardar la partida')
        print('[0] - Salir de la partida')

        inpt = self.recibir_input()


        if inpt == '1':
            self.iniciar_carrera()
        elif inpt == '2':
            self.comprar_vehiculos()
        elif inpt == '3':
            self.guardar_partida()
            self.menu()
        elif inpt == '0':
            print('Deseas guardar la partida antes de salir?')
            print('[1] - Si')
            print('[0] - No')
            resp = self.recibir_input()
            if resp == '1':
                self.guardar_partida()
                self.volver_menu()
            elif resp == '0':
                self.volver_menu()

        else:
            print('Respuesta invalida, por favor indique nuevamente.')
    




class MenuCompras(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto


    def volver_menu(self):
        menu = MenuPrincipal(self.piloto)
        menu.menu()
        

        
    def menu(self):
        print(self._menu)

        print('Bienvenido al Almacen DCCoches!')
        print('Espero que encuentres lo que buscas!')
        print('Por favor, indica el numero del vehiculo que quieras comprar!')
        print('Tenemos los siguientes vehiculos: ')
        print('[1] - Automoviles        $550')
        print('[2] - Troncomovil        $900')
        print('[3] - Motocicleta        $370')
        print('[4] - Bicicleta          $1.050')
        print('[5] - Ver el garage          ')
        print('Dinero disponible: {0}'.format(self.piloto.dinero))
        inpt = self.recibir_input()

        if inpt == '0':
            self.volver_menu()
        elif inpt == '1' or inpt == '2' or inpt == '3' or inpt == '4':
            self.compra(inpt)
        elif inpt == '5':
            for v in self.piloto.vehiculos:
                print(v)
            self.menu()
        else:
            print('Respuesta invalida, por favor indique nuevamente.')
            self.menu()


    def compra(self, tipo):
        if tipo == '1':
            nombre = input('Por favor indique el nombre de su nuevo automovil:   ')
            existe = self.verificar_vehiculo(nombre)
            if existe == 1:
                print('Nombre del vehiculo ya existe o no es valido.')
                self.compra(tipo)
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

                vehiculo = Automovil(nombre, self.piloto.nombre, 
                    chasis, carroceria, ruedas, motor, peso)
                self.piloto.vehiculos.append(vehiculo)
                self.piloto.dinero -= 550
                self.menu()

        elif tipo == '2':
            nombre = input('Por favor indique el nombre de su nuevo automovil')
            existe = self.verificar_vehiculo(nombre)
            if existe == 1:
                print('Nombre del vehiculo ya existe o no es valido.')
                self.compra(tipo)
            else:
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

                vehiculo = Troncomovil(nombre, self.piloto.nombre, 
                    chasis, carroceria, ruedas, zapatillas, peso)
                self.piloto.vehiculos.append(vehiculo)
                self.piloto.dinero -= 900
                self.menu()

        elif tipo == '3':
            nombre = input('Por favor indique el nombre de su nuevo automovil')
            existe = self.verificar_vehiculo(nombre)
            if existe == 1:
                print('Nombre del vehiculo ya existe o no es valido.')
                self.compra(tipo)
            else:

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

                vehiculo = Motocicleta(nombre, self.piloto.nombre, 
                    chasis, carroceria, ruedas, motor, peso)
                self.piloto.vehiculos.append(vehiculo)
                self.piloto.dinero -= 370
                self.menu()

        else:
            nombre = input('Por favor indique el nombre de su nuevo automovil')
            existe = self.verificar_vehiculo(nombre)
            if existe == 1:
                print('Nombre del vehiculo ya existe o no es valido.')
                self.compra(tipo)
            else:
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

                vehiculo = Bicicleta(nombre, self.piloto.nombre, 
                    chasis, carroceria, ruedas, zapatillas, peso)
                self.piloto.vehiculos.append(vehiculo)
                self.piloto.dinero -= 1050
                self.menu()
