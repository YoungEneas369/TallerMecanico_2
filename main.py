# main.py
from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion

v1 = Vehiculo("KXPR84", 2019)
v1.ingresar()
print(v1.patente, v1.anio, v1.tarifa_hora())

# Demostración de herencia: Auto, Moto y Camion heredan todo de Vehiculo
auto1 = Auto("AB12CD", 2021)
moto1 = Moto("XY98", 2023)
camion1 = Camion("TR77ZZ", 2018)

auto1.ingresar()
moto1.ingresar()
camion1.ingresar()

print("Auto:", auto1.patente, auto1.anio, auto1.tarifa_hora(), "¿en taller?:", auto1._en_taller)
print("Moto:", moto1.patente, moto1.anio, moto1.tarifa_hora(), "¿en taller?:", moto1._en_taller)
print("Camión:", camion1.patente, camion1.anio, camion1.tarifa_hora(), "¿en taller?:", camion1._en_taller)
