"""
Aquí debes completar las funciones del Bonus
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""

TECH_KEYS = {
    'Piso -1': ['red', 'yellow', 'blue', 'purple', 'blue', 'purple', 'green', 'red', 'orange'],
    'Piso -2': ['black', 'pink', 'blue', 'green', 'green', 'orange', 'grey', 'red', 'yellow'],
    'Piso -3': ['purple', 'grey', 'orange', 'red', 'purple', 'pink', 'purple', 'grey',
                'orange', 'red', 'purple', 'pink'],
    'Piso -4': ['blue', 'red', 'white', 'green', 'blue', 'white', 'lightblue', 'white',
                'yellow', 'blue', 'red', 'yellow', 'purple', 'yellow', 'red', 'orange',
                'black', 'white', 'grey']
}


def cargar_llaves(ruta_archivo_llaves):
    print(f"Cargando datos de {ruta_archivo_llaves}...")
    llaves = {
        'Piso -1': '',
        'Piso -2': '',
        'Piso -3': '',
        'Piso -4': ''
    }
    with open(ruta_archivo_llaves, 'r', encoding='utf-8') as archivo:
        for line in archivo:
            piso, llave = line.split(';')
            combinacion = llave.strip().split(',')
            llaves[piso] = combinacion
    
    return llaves


def desbloquear_pisos(llaves, piso):
    if llaves[piso] == TECH_KEYS[piso]:
        return True
    else:
        return False
    

