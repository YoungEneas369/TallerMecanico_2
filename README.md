# 🚗 Proyecto Taller Mecánico 2

¡Bienvenido a este proyecto! Aquí aprenderemos paso a paso cómo crear y gestionar vehículos utilizando **Programación Orientada a Objetos (POO)** en Python.

---

## 🧒 Explicación paso a paso (¡como para un niño!)

### 1. ¿Qué es una Clase? (El molde de galletas 🍪)
Imagina que quieres hacer galletitas con forma de auto.
* La **Clase** (`Vehiculo`) es el **molde cortador**: por sí sola no es una galleta comestible, es solo la forma y las instrucciones que dicen qué partes tendrá cada galleta.
* El archivo [vehiculo.py](vehiculo.py) contiene este molde.

### 2. Declaración de Atributos (Las características del molde 📋)
Antes de construir el auto, definimos qué cosas debe tener todo vehículo:
* `patente: str`: Un texto para identificar el auto (su matrícula).
* `anio: int`: Un número entero que indica el año de fabricación.
* `_en_taller: bool`: Un valor de verdadero o falso (`True` o `False`) que nos dice si el auto está siendo reparado dentro del taller.

> **Ojo:** Esto no crea ningún auto todavía, solo avisa qué datos usará el molde.

### 3. El Constructor `__init__` (La fábrica que crea el auto 🏭)
Cuando usamos el molde para crear un auto de verdad en la memoria de la computadora:
* Le entregamos la **patente** y el **año** (son parámetros obligatorios).
* El atributo `_en_taller` **NO se pide por parámetro**: siempre se fija automáticamente en `False`. ¿Por qué? ¡Porque cuando recién compramos o registramos un auto, no parte descompuesto dentro del taller!

### 4. Creando nuestro primer vehículo en `main.py` 🚘
En el archivo [main.py](main.py):
1. Importamos el molde `Vehiculo`.
2. Creamos un auto real con patente `'KXPR84'` y año `2019`.
3. Usamos `print()` para ver sus datos en pantalla.

---

## 📁 Archivos del Proyecto

* **[vehiculo.py](vehiculo.py)**: Define la clase `Vehiculo` con su molde, tipos de datos y constructor `__init__`.
* **[main.py](main.py)**: Archivo principal de prueba donde creamos el objeto y mostramos sus valores por consola.
* **[README.md](README.md)**: Esta guía explicativa.

---

## 🚀 ¿Cómo probar el código en tu computadora?

Abre una terminal en esta carpeta y ejecuta:

```bash
python main.py
```

### Salida esperada en la consola:
```text
Patente: KXPR84
Año: 2019
¿Está en el taller?: False
```