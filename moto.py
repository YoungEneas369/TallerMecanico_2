# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo

# Define la clase Moto que hereda de la clase base Vehiculo
class Moto(Vehiculo):
    # Método que retorna la tarifa por hora específica para motos
    def tarifa_hora(self) -> int:
        return 20000