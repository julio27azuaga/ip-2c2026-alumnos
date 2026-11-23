from ..utilidades.horas import horaAMinutos
from ..utilidades.textos import normalizar
from ...configuracion import POSICION_HORA_INICIO, TURNOS


def turnoDe(horario):

    hora_inicio = horario[POSICION_HORA_INICIO]
    if not hora_inicio:
        return ""

    minutos_inicio = horaAMinutos(hora_inicio)

    for nombre_turno, inicio_turno, fin_turno in TURNOS:
        if horaAMinutos(inicio_turno) <= minutos_inicio <= horaAMinutos(fin_turno):
            return nombre_turno

    return ""


def filtrarPorTurno(horarios, turno):
 
    resultados = []
    turno_buscado = normalizar(turno)

    for horario in horarios:
        if normalizar(turnoDe(horario)) == turno_buscado:
            resultados.append(horario)

    return resultados
