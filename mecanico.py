# mecanico.py
# Esta clase representa el molde para registrar mecánicos en el taller.

class Mecanico:
    # Declaración de atributos con sus tipos:
    nombre: str        # Texto: nombre del mecánico
    especialidad: str  # Texto: ej. "Frenos", "Motores", "Electricidad"
    _ocupado: bool     # Booleano: True si está atendiendo un auto, False si está libre

    def __init__(self, nombre: str, especialidad: str) -> None:
        # El constructor recibe solo nombre y especialidad al crearse
        self.nombre = nombre
        self.especialidad = especialidad
        # Por defecto siempre parte disponible (desocupado)
        self._ocupado = False

    def asignar_trabajo(self) -> None:
        """Marca al mecánico como ocupado atendiendo un trabajo."""
        self._ocupado = True

    def liberar(self) -> None:
        """Libera al mecánico para que quede disponible nuevamente."""
        self._ocupado = False

    def tarifa_hora(self) -> int:
        """Retorna el costo base por hora de la mano de obra del mecánico."""
        return 18000
