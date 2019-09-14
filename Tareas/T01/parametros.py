import os


# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 200,
        'MAX': 400
    },
    'CARROCERIA': {
        'MIN': 150,
        'MAX': 400
    },
    'RUEDAS': {
        'MIN': 38,
        'MAX': 70
    },
    'MOTOR': {
        'MIN': 100,
        'MAX': 400
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 600,
        'MAX': 1000
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 90,
        'MAX': 120
    },
    'CARROCERIA': {
        'MIN': 80,
        'MAX': 120
    },
    'RUEDAS': {
        'MIN': 35,
        'MAX': 60
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 80,
        'MAX': 120
    },
    'PESO': {
        'MIN': 100,
        'MAX': 370
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 60,
        'MAX': 90
    },
    'CARROCERIA': {
        'MIN': 35,
        'MAX': 75
    },
    'RUEDAS': {
        'MIN': 15,
        'MAX': 45
    },
    'MOTOR': {
        'MIN': 30,
        'MAX': 55
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 90,
        'MAX': 200
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 20,
        'MAX': 40
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 30
    },
    'RUEDAS': {
        'MIN': 1,
        'MAX': 20
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 20,
        'MAX': 40
    },
    'PESO': {
        'MIN': 30,
        'MAX': 60
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': None,
        'EFECTO': None
    },
    'CARROCERIA': {
        'COSTO': None,
        'EFECTO': None
    },
    'RUEDAS': {
        'COSTO': None,
        'EFECTO': None
    },
    'MOTOR': {
        'COSTO': None,
        'EFECTO': None
    },
    'ZAPATILLAS': {
        'COSTO': None,
        'EFECTO': None
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': 'precavido'
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': ['precavido', 'osado']
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': 'osado'
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = None

# Velocidad intencional
EFECTO_OSADO = None
EFECTO_PRECAVIDO = None

# Dificultad de control del vehículo
PESO_MEDIO = None
EQUILIBRIO_PRECAVIDO = None

# Tiempo pits
TIEMPO_MINIMO_PITS = None
VELOCIDAD_PITS = None

# Experiencia por ganar
BONIFICACION_PRECAVIDO = None
BONIFICACION_OSADO = None


# Paths de los archivos

PATHS = {
    'PISTAS': os.path.join('base_datos', 'pistas.csv'),
    'CONTRINCANTES': os.path.join('base_datos', 'contrincantes.csv'),
    'PILOTOS': os.path.join('base_datos', 'pilotos.csv'),
    'VEHICULOS': os.path.join('base_datos', 'vehículos.csv'),
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None





#Dinero Inicial de los Pilotos creados
DINERO_INI = 500