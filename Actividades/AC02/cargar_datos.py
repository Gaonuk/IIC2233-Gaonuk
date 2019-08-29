"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""
import csv
from collections import deque
from collections import namedtuple


"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""
Alumno = namedtuple('Alumno_type', ['nombre', 'habilidades'])
Ayudante = namedtuple('Ayudante_type', ['nombre', 'rango', 'debilidades', 'comiendo'])

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    alumnos = list()
    with open(ruta_archivo_alumnos, 'r', encoding='utf-8') as archivo:
        for line in archivo:
            nombre, habilidades = line.split(';')
            habilidades = habilidades.strip().split(',')
            habis = set()
            for habilidad in habilidades:
                habis.add(habilidad)
            
            alumno = Alumno(nombre, habis)
            alumnos.append(alumno)

    return alumnos


def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    ayudantes = []
    with open(ruta_archivo_ayudantes, 'r', encoding='utf-8') as archivo:
        for line in archivo:
            nombre, rango, debilidades = line.split(';')
            debilidades = debilidades.strip().split(',')
            debis = set()
            for debilidad in debilidades:
                debis.add(debilidad)
            comiendo = []
            ayudante = Ayudante(nombre, rango, debis, comiendo)
            ayudantes.append(ayudante)
    
    ayudantes_por_piso = {
        'Piso -1': '',
        'Piso -2': '',
        'Piso -3': '',
        'Piso -4': ''
    }
    ayudantes1 = deque()
    ayudantes2 = deque()
    ayudantes3 = deque()
    ayudantes4 = deque()
    for ayudante in ayudantes:
        if ayudante.rango == 'Chief Tamburini':
            ayudantes4.append(ayudante)
        elif ayudante.rango == 'Jefe':
            ayudantes3.append(ayudante)
        elif ayudante.rango == 'Mentor':
            ayudantes2.append(ayudante)
        elif ayudante.rango == 'Nuevo':
            ayudantes1.append(ayudante)
    
    ayudantes_por_piso['Piso -1'] = ayudantes1
    ayudantes_por_piso['Piso -2'] = ayudantes2
    ayudantes_por_piso['Piso -3'] = ayudantes3
    ayudantes_por_piso['Piso -4'] = ayudantes4

    return ayudantes_por_piso