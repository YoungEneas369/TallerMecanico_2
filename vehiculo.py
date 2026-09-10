# vehiculo.py
# Esta clase representa solo el molde (plantilla) para crear vehículos más adelante.

class Vehiculo:
    # Declaración de atributos con sus tipos (indicando qué tendrá cada vehículo):
    patente: str      # Texto: la patente del vehículo
    anio: int         # Número entero: el año de fabricación del vehículo
    _en_taller: bool  # Booleano (True o False): indica si el vehículo está actualmente en el taller

    def __init__(self, patente: str, anio: int) -> None:
        # El método __init__ es el constructor: se ejecuta automáticamente al crear un nuevo vehículo.
        # Guarda la patente que recibimos como parámetro en el atributo propio del vehículo.
        self.patente = patente
        # Guarda el año que recibimos como parámetro en el atributo propio del vehículo.
        self.anio = anio
        # Fija _en_taller siempre en False por defecto, ya que un vehículo recién registrado nunca parte dentro del taller.
        self._en_taller = False
