from os.path import join
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

PATHS = {
    'mapa_1': join('mapas', 'mapa_1.txt'),
    'mapa_2': join('mapas', 'mapa_2.txt'),
    'store': join('sprites/mapa', 'store.png'),
    'house': join('sprites/mapa', 'house.png'),
    'roca': join('sprites/mapa', 'tile030.png'),
    'tile': join('sprites/mapa', 'tile006.png'),
    'flores': join('sprites/mapa', 'tile000.png'),
    'cultivo': join('sprites/mapa', 'tile020.png'),
    'fondo': join('sprites/otros', 'window_template.jpg'),
    'inventario': join('sprites/otros', 'invetary_template.jpg'),
    'logo': join('sprites/otros', 'logo.png'),
    'azada': join('sprites/otros', 'hoe.png'),
    'hacha': join('sprites/otros', 'axe.png'),
    'semilla_a': join('sprites', 'cultivos', 'alcachofa', 'seeds.png'),
    'semilla_c': join('sprites', 'cultivos', 'choclo', 'seeds.png'),
    'choclo': join('sprites', 'cultivos', 'choclo', 'icon.png'),
    'alcachofa': join('sprites', 'cultivos', 'alcachofa', 'icon.png'),
    'oro': join('sprites', 'recursos', 'gold.png'),
    'madera': join('sprites', 'recursos', 'wood.png'),
    'arbol': join('sprites/otros', 'tree.png')
}

SIZE_TILE = 32

PERSONAJE = {
    ('D', 1): join('sprites/personaje', 'down_1.png'),
    ('D', 2): join('sprites/personaje', 'down_2.png'),
    ('D', 3): join('sprites/personaje', 'down_3.png'),
    ('D', 4): join('sprites/personaje', 'down_4.png'),
    ('L', 1): join('sprites/personaje', 'left_1.png'),
    ('L', 2): join('sprites/personaje', 'left_2.png'),
    ('L', 3): join('sprites/personaje', 'left_3.png'),
    ('L', 4): join('sprites/personaje', 'left_4.png'),
    ('R', 1): join('sprites/personaje', 'right_1.png'),
    ('R', 2): join('sprites/personaje', 'right_2.png'),
    ('R', 3): join('sprites/personaje', 'right_3.png'),
    ('R', 4): join('sprites/personaje', 'right_4.png'),
    ('U', 1): join('sprites/personaje', 'up_1.png'),
    ('U', 2): join('sprites/personaje', 'up_2.png'),
    ('U', 3): join('sprites/personaje', 'up_3.png'),
    ('U', 4): join('sprites/personaje', 'up_4.png'),

}

CHOCLO = {
    1: join('sprites/cultivos/choclo', 'stage_1'),
    2: join('sprites/cultivos/choclo', 'stage_2'),
    3: join('sprites/cultivos/choclo', 'stage_3'),
    4: join('sprites/cultivos/choclo', 'stage_4'),
    5: join('sprites/cultivos/choclo', 'stage_5'),
    6: join('sprites/cultivos/choclo', 'stage_6')
}

KEY_EVENT_DICT = {
        Qt.Key_D: 'R',
        Qt.Key_A: 'L',
        Qt.Key_W: 'U',
        Qt.Key_S: 'D'
    }

DINERO_INICIAL = 100

DINERO_TRAMPA = 50

FONT = QFont('Times', 16)