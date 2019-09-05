import os


# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
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
            'MIN': None,
            'MAX': None
        },
        'EQUILIBRIO': {
            'MIN': None,
            'MAX': None
        },
        'PERSONALIDAD': None
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': None,
            'MAX': None
        },
        'EQUILIBRIO': {
            'MIN': None,
            'MAX': None
        },
        'PERSONALIDAD': None
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': None,
            'MAX': None
        },
        'EQUILIBRIO': {
            'MIN': None,
            'MAX': None
        },
        'PERSONALIDAD': None
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
