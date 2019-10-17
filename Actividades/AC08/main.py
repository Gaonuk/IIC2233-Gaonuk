from cargar import cargar_archivos
from os import path


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        self.nodos = dict()

    def nuevo_usuario(self, id_usuario, nombre):
        if not self.nodos.get(id_usuario):
            self.nodos[id_usuario] = Usuario(id_usuario, nombre)

    def follow(self, id_seguidor, id_seguido):
        if id_seguido in self.nodos[id_seguidor].seguidos:
            print('Ya lo estas siguiendo')
        else:
            self.nodos[id_seguidor].seguidos.append(id_seguido)


    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        for usuario, nombre, seguidos in cargar_archivos(ruta_red):
            self.nuevo_usuario(usuario, nombre)
            for seguido in seguidos:
                self.follow(usuario, seguido)
            

    def unfollow(self, id_seguidor, id_seguido):
        if not id_seguido in self.nodos[id_seguidor].seguidos:
            print('No estas siguiendo a este usuario')
        else:
            self.nodos[id_seguidor].seguidos.remove(id_seguido)

    def mis_seguidos(self, id_usuario):
        num_seguidos = 0
        for seguidos in self.nodos[id_usuario].seguidos:
            num_seguidos += 1
        return num_seguidos

    def distancia_social(self, origen, destino):
        # Método que retorna la "distancia social" de dos usuarios
        visitados = set()  # Guardamos los nodos ya visitados
        stack = [self.nodos[origen]]  # Ordena el recorrido con un stack

        boolean = False
        distancia = 0
        while len(stack) > 0:  # Mientras queden nodos visitables
            usuario_actual = stack.pop()  # Sacamos el último agregado
            if usuario_actual not in visitados:  # Importante check visitados
                visitados.add(usuario_actual)  # Registramos como visitado
                if usuario_actual.id == destino:  # Check llegamos al destino
                    boolean = True
                    break
                distancia += 1
                # Vecinos del nodo actual
                for seguido in usuario_actual.seguidos:
                    if seguido not in visitados:  # Importante check visitados x2
                        stack.append(self.nodos[seguido])  # Agregamos vecinos al stack

        return boolean, distancia


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    # print(pintogram.mis_seguidos("13"))
    # print(pintogram.mis_seguidos("7"))
    # print(pintogram.mis_seguidos("18"))
    # print(pintogram.mis_seguidos("10"))
    # print(pintogram.mis_seguidos("20"))
    # print(pintogram.mis_seguidos("25"))
    print(pintogram.distancia_social("3", "5"))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
