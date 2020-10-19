from leer_archivos import read_file
from collections import deque, defaultdict

class Ayudante:

    jerarquia = {
        'Coordinador': 'Jefe',
        'Jefe': 'Mentor',
        'Mentor': 'Novato',
        'Novato': None
    }

    def __init__(self, nombre, rango, tipo, afinidad, eficiencia):
        self.nombre = nombre
        self.rango = rango
        self.tipo = tipo
        self.afinidad = afinidad
        self.eficiencia = int(eficiencia)
        self.hijos = []

    def agregar_ayudante(self, ayudante):
        if ayudante.rango == Ayudante.jerarquia[self.rango]:
            if ayudante.tipo == self.tipo:
                self.hijos.append(ayudante)
            elif self.tipo == 'Coordinador':
                self.hijos.append(ayudante)
            else:
                pass
        else:
            for hijo in self.hijos:
                if ayudante.tipo == hijo.tipo:
                    hijo.agregar_ayudante(ayudante)
            


def grupo_mayor_eficiencia(coordinador):
    inicial = coordinador
    tareo = coordinador.hijos[0]
    docencio = coordinador.hijos[1]
    visitados = []
    e_tareos = 4 * coordinador.eficiencia
    e_docencios = 4 * coordinador.eficiencia
    queue = deque([inicial])
    while len(queue) > 0:
        vertice = queue.popleft()
        if vertice not in visitados:
            aumento = vertice.eficiencia
            if vertice.tipo == 'Tareos':
                if vertice.rango == 'Jefe':
                    aumento = 3 * aumento
                    e_tareos += aumento
                elif vertice.rango == 'Mentor':
                    aumento = 2 * aumento
                    e_tareos += aumento
                elif vertice.rango == 'Novato':
                    e_tareos += aumento
            else:
                if vertice.rango == 'Jefe':
                    aumento = 3 * aumento
                    e_docencios += aumento
                elif vertice.rango == 'Mentor':
                    aumento = 2 * aumento
                    e_docencios += aumento
                elif vertice.rango == 'Novato':
                    e_docencios += aumento
            visitados.append(vertice)
            for vecino in vertice.hijos:
                if vecino not in visitados:
                    queue.append(vecino)
    
    if e_docencios > e_tareos:
        imprimir_grupo(docencio)
        print('Grupo mas eficiente: Docencios')
        print(f'Eficiencia total grupal: {e_docencios}')
    else:
        imprimir_grupo(tareo)
        print('Grupo mas eficiente: Tareos')
        print(f'Eficiencia total grupal: {e_tareos}')



def imprimir_grupo(ayudante):
    inicial = ayudante
    visitados = []
    todos = defaultdict(str)
    queue = deque([inicial])
    while len(queue) > 0:
        vertice = queue.popleft()
        if vertice not in visitados:
            todos[vertice.rango] += f'{vertice.nombre}, '
            visitados.append(vertice)
            for vecino in vertice.hijos:
                if vecino not in visitados:
                    queue.append(vecino)


    print('Coordinador: ', 'Enzo Tamburini')
    print('Jefe: ', todos['Jefe'])
    print('Mentor: ',todos['Mentor'])
    print('Novato: ', todos['Novato'])     
    
        


def instanciar_cuerpo_ayudantes(ayudantes):
    # No modificar
    enzini = Ayudante(**ayudantes[0])
    for data in ayudantes[1:]:
        enzini.agregar_ayudante(Ayudante(**data))
    return enzini


if __name__ == "__main__":
    # No modificar
    ayudantes = read_file()
    cuerpo_ayudantes = instanciar_cuerpo_ayudantes(ayudantes)
    grupo_mayor_eficiencia(cuerpo_ayudantes)
