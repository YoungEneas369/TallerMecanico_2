# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Define la clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):
    # Método que retorna la tarifa por hora específica para camiones
    def tarifa_hora(self) -> int:
        return 40000