from collections import namedtuple
from parametros import *
from math import floor, ceil


def velocidad_intencional(personalidad, vel_recomendada):
    if personalidad == 'osado':
        return EFECTO_OSADO * vel_recomendada   
    elif personalidad == 'precavido':
        return EFECTO_PRECAVIDO * vel_recomendada

def calcular_hipotermia(contextura, numero_vuelta, hielo_pista):
    if contextura < hielo_pista:
        return (contextura - hielo_pista) * numero_vuelta
    else:
        return 0


def vel_recomendada(vel_base, traccion, defensa, 
    experiencia, hielo, rocas, dificultad):
    return vel_base + (traccion - hielo)*POND_EFECT_HIELO + \
        (defensa - rocas)*POND_EFECT_ROCAS + \
        (experiencia - dificultad)*POND_EFECT_DIFICULTAD


def vel_real(self, vel_intencional, control, hipotermia):
    if VELOCIDAD_MINIMA > (vel_intencional + control + hipotermia):
        return VELOCIDAD_MINIMA
    else:
        return vel_intencional + control + hipotermia

def dificultad_control(piloto, vehiculo):
    if vehiculo.ruedas == 2 and piloto.personalidad == 'osado':
        if (piloto.equilibrio - floor(PESO_MEDIO/vehiculo.peso)) > 0:
            return 0
        else:
            return piloto.equilibrio - floor(PESO_MEDIO/vehiculo.peso)
    
    elif vehiculo.ruedas == 2 and piloto.personalidad == 'precavido':
        if (piloto.equilibrio*EQUILIBRIO_PRECAVIDO 
            - floor(PESO_MEDIO/vehiculo.peso)) > 0:
            return 0
        else:
            return (piloto.equilibrio*EQUILIBRIO_PRECAVIDO 
                - floor(PESO_MEDIO/vehiculo.peso))
    
    else:
        return 0

def dmg_vehiculo(rocas, defensa):
    if (rocas - defensa) > 0:
        return rocas - defensa
    else:
        return 0

def tiempo_pits(dura_inic_chasis, dura_act_chasis):
    return TIEMPO_MINIMO_PITS + (dura_inic_chasis - 
        dura_act_chasis)*VELOCIDAD_PITS


def dinero_vuelta(vuelta, dificultad):
    return vuelta*dificultad


def prob_accidente(vel_real, vel_recomendada, dur_max_chasis, dura_act_chasis):
    if ((vel_real - vel_recomendada) / vel_recomendada) < 0:
        if floor((dur_max_chasis - dura_act_chasis) / dur_max_chasis) > 1:
            return 1
        else:
            return floor((dur_max_chasis - dura_act_chasis) / dur_max_chasis)
    else:
        if ((vel_real - vel_recomendada) / vel_recomendada) + \
            floor((dur_max_chasis - dura_act_chasis) / dur_max_chasis) > 1:
            return 1
        else:
            return ((vel_real - vel_recomendada) / vel_recomendada) + \
            floor((dur_max_chasis - dura_act_chasis) / dur_max_chasis)


def tiempo_vuelta(largo, vel_real):
    return ceil(largo/vel_real)

def dinero_ganador(total_vueltas, dificultad, hielo, rocas):
    return total_vueltas*(dificultad + hielo + rocas)

def ventaja(tiempo_primero, tiempo_ultimo):
    return tiempo_ultimo - tiempo_primero

def experiencia_ganar(personalidad, ventaja, dificultad):
    if personalidad == 'precavido':
        return (ventaja + dificultad)*BONIFICACION_PRECAVIDO
    else:
        return (ventaja + dificultad)*BONIFICACION_OSADO

