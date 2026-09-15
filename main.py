# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo
# Importa la clase derivada Auto desde el módulo auto
from auto import Auto
# Importa la clase derivada Moto desde el módulo moto
from moto import Moto
# Importa la clase derivada Camion desde el módulo camion
from camion import Camion

# Instancia objetos de las clases derivadas
a = Auto("auto1234", 2020)
m = Moto("moto1234", 2021)
c = Camion("camion1234", 2019)

# Registra el ingreso del objeto Auto al taller cambiando su estado interno
a.ingresar_al_taller()

# Muestra en consola la patente del auto instanciado
print("Patente auto:", a.patente)
print("Auto en taller:", a._en_taller)

# Muestra en consola las tarifas por hora de cada tipo de vehículo
print("Tarifa Moto:", m.tarifa_hora())
print("Tarifa Auto:", a.tarifa_hora())
print("Tarifa Camión:", c.tarifa_hora())

# Registra la entrega del vehículo al cliente cambiando su estado interno
a.entregar_al_cliente()
print("Auto en taller:", a._en_taller)