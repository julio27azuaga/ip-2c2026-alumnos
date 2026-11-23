from ...configuracion import ( DIA_VIRTUAL, POSICION_DIA, POSICION_HORA_INICIO, POSICION_HORA_FIN)
from ..utilidades.horas import horaAMinutos


def seSuperponen(horarioA, horarioB):
    dia_a = horarioA[POSICION_DIA]
    dia_b = horarioB[POSICION_DIA]

    # Verifica los horarios no sean virtuales
    if dia_a == DIA_VIRTUAL or dia_b == DIA_VIRTUAL:
        return False

    # Verifica que ambos horarios sean diferentes
    if dia_a != dia_b:
        return False

    # Verifica que los horarios sean virtuales, si lo son no se superponen
    if not horarioA[POSICION_HORA_INICIO] or not horarioA[POSICION_HORA_FIN]:
        return False
    if not horarioB[POSICION_HORA_INICIO] or not horarioB[POSICION_HORA_FIN]:
        return False

    # Guardo las horas de inicio y fin de los horarios para comparalos
    inicio_a = horaAMinutos(horarioA[POSICION_HORA_INICIO])
    fin_a = horaAMinutos(horarioA[POSICION_HORA_FIN])

    inicio_b = horaAMinutos(horarioB[POSICION_HORA_INICIO])
    fin_b = horaAMinutos(horarioB[POSICION_HORA_FIN])

    # verifica si los horarios se superponen y devuelve la respuesta
    return inicio_a < fin_b and inicio_b < fin_a


def buscarSuperposiciones(horariosA, horariosB):
    pares = []

    # Recorre los horarios y los compara para ver si se superponen
    for horario_a in horariosA:
        for horario_b in horariosB:
            if seSuperponen(horario_a, horario_b):
                pares.append([horario_a,horario_b])
    
    return pares
