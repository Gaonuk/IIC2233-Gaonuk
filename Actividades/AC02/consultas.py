"""
Aquí debes completar las funciones de las consultas
"""
from collections import defaultdict

def resumen_actual(ayudantes, alumnos):
    print('-'*20)
    print('Alumnos restantes: {0}'.format(len(alumnos)))
    ayudantes_totales = 0
    ayudantes_totales += len(ayudantes['Piso -1'])
    ayudantes_totales += len(ayudantes['Piso -2'])
    ayudantes_totales += len(ayudantes['Piso -3'])
    ayudantes_totales += len(ayudantes['Piso -4'])
    print('Ayudantes restantes: {0}'.format(ayudantes_totales))
    print('Ayudantes Piso -1: {0}'.format(len(ayudantes['Piso -1'])))
    print('Ayudantes Piso -2: {0}'.format(len(ayudantes['Piso -2'])))
    print('Ayudantes Piso -3: {0}'.format(len(ayudantes['Piso -3'])))
    print('Ayudantes Piso -4: {0}'.format(len(ayudantes['Piso -4'])))
    print('-'*20)
    


def stock_comida(alumnos):
    stock = []
    comidas = dict()

    for alumno in alumnos:
        for comida in alumno.habilidades:
            habilidad = comida
            if habilidad not in comidas:
                comidas[habilidad] = 0
            comidas[habilidad] += 1

    for par in comidas.items():
        stock.append(par)

    return stock
