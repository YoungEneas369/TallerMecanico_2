# main.py
# Importamos la clase Vehiculo desde el archivo vehiculo.py
from vehiculo import Vehiculo

# Creamos una instancia (objeto) de Vehiculo con patente 'KXPR84' y año 2019
auto1 = Vehiculo(patente="KXPR84", anio=2019)

# Mostramos por consola los valores usando print()
print(f"Patente: {auto1.patente}")
print(f"Año: {auto1.anio}")
print(f"¿Está en el taller?: {auto1._en_taller}")
