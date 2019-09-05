from parametros import PATHS


#Creacion de clases 
class Menu():
    def __init__(self):
        self._menu =    "    ____            _            _             __           ____  \n" + \
                        "   /  _/   ____    (_)  _____   (_)  ____ _   / /          / __ \ \n" + \
                        "   / /    / __ \  / /  / ___/  / /  / __ `/  / /          / /_/ / \n" + \
                        " _/ /    / / / / / /  / /__   / /  / /_/ /  / /          / ____/  \n" + \
                        "/___/   /_/ /_/ /_/   \___/  /_/   \__,_/  /_/          /_/       \n"

    #Este es un metodo comun para que todos los menus puedan 
    #recibir inputs 
    def recibir_input(self):
        inpt = input('Por favor, indique su respuesta: (0 para salir) ')
        return inpt
    
class MenuSesion(Menu):
    def __init__(self):
        super().__init__()


    def crear_piloto(self):
        piloto = input('Por favor indique su nombre de piloto:    ')
        if not piloto.isalnum():
            print('Nombre de piloto no valido.')
            self.crear_piloto()
        else:
            existe = 0
            with open(PATHS['PILOTOS'], 'r', encoding='utf-8') as archivo:
                for line in archivo:
                    if line == piloto:
                        existe = 1

            if existe == 1:
                print('Nombre de piloto ya existe.')
                self.crear_piloto()
            else:
                pass


    def crear_partida(self):
        piloto = self.crear_piloto()
        menu1 = MenuPrincipal(piloto)
        menu1.menu()


    def cargar_partida(self, ruta, piloto):
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for line in archivo:
                if line.split(',')[0] == piloto:
                    pass


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
            pass
        else:
            print('Respuesta invalida, por favor indique nuevamente.')
            self.menu()
        


class MenuPrincipal(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
    

    def iniciar_carrera(self):
        menu_carrera = MenuCarrera()
        menu_carrera.menu()


    def comprar_vehiculos(self):
        menu_compras = MenuCompras(self.piloto)
        menu_compras.menu()


    def guardar_partida(self):
        pass


    def volver_menu(self):
        menu_sesion = MenuSesion()
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
        elif inpt == '0':
            print('Deseas guardar la partida antes de salir?')
            print('[0] - Si')
            print('[1] - No')
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
        print('\n')
        print('Dinero disponible: {0}'.format(self.piloto.dinero))
        inpt = self.recibir_input()

        if inpt == '0':
            self.volver_menu()
        elif inpt == '1' or inpt == '2' or inpt == '3' or inpt == '4':
            self.compra(inpt)
        else:
            print('Respuesta invalida, por favor indique nuevamente.')
            self.menu()


    def compra(self, vehiculo):
        pass

class MenuPreparacion(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
    


class MenuCarrera(Menu):
    def __init__(self):
        super().__init__()


    def menu(self):
        print()


class MenuPits(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto

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