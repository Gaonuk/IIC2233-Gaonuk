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