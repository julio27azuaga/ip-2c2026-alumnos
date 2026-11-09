from ... import configuracion
from ... import PROGRAMACION_07, PROGRAMACION_07_VIRTUAL, PROGRAMACION_13, ALGEBRA_02, OFERTA

def turnoDe(horario):
    """OPCIONAL. Recibe un horario.
    Se fija en qué turno empieza, según TURNOS en configuracion.py.
    Devuelve "mañana", "tarde" o "noche", o "" si el horario es virtual.
    Ejemplo: un horario que empieza a las 18:00 devuelve "noche".
    
    En base a lo que el usuario setee en 'oferta', se recorrerá (primero) la colección de TURNOS y por cada elemento de la lista, consultará si hay
    o no coincidencia entre el horario recibido y el horario de inicio del turno. En caso de encontrar coincidencia, se devolverá el nombre del turno correspondiente.
    En caso de no encontrar coincidencia, se devolverá un string vacío.


    
    """
    TURNOS=[
  ["mañana", "08:00", "12:59"],
  ["tarde", "13:00", "17:59"],
  ["noche", "18:00", "23:59"],
    ]
    actual=""
    for turno in range(len(TURNOS)):
        if TURNOS[turno][1].startswith(horario):
            actual=TURNOS[turno]
            return actual[0]


    return actual


def filtrarPorTurno(horarios, turno):
  """OPCIONAL. Recibe una lista de horarios y un turno ("mañana", "tarde" o "noche").
            Se queda con los horarios que empiezan en ese turno.
            Devuelve la lista de esos horarios, o una lista vacía si no hay ninguno.
            Ejemplo: con los horarios de Álgebra I y "noche", devuelve el de la COM-02 (miércoles 18:00).
    """

  TURNOS = [
     ["mañana", "08:00", "12:59", PROGRAMACION_07],
     ["tarde", "13:00", "17:59", PROGRAMACION_13],
     ["noche", "18:00", "23:59", ALGEBRA_02],
     ["mañana", "08:00", "12:59", PROGRAMACION_07_VIRTUAL],
     ["tarde", "13:00", "17:59", PROGRAMACION_13],
     ["noche", "18:00", "23:59", ALGEBRA_02]
     ]

  OFERTA

  turnosCoincidentes = []
 
  return []