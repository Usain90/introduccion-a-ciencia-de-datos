# ============================================================
# Variables y Tipos de Datos en Python
# ============================================================

# 1️⃣ Declaración de variables
# En Python no es necesario especificar el tipo de dato.
# El intérprete lo detecta automáticamente según el valor asignado.

nombre = "Usain"     # str (cadena de texto)
edad = 35            # int (entero)
altura = 1.87        # float (decimal)
activo = True        # bool (booleano)




print("Datos personales:")
print(nombre, edad, altura, activo)
print()  # línea vacía

type(edad)

# ------------------------------------------------------------
# 2️⃣ Comprobando el tipo de dato con type()
print("Tipos de datos:")
print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>
print(type(altura))   # <class 'float'>
print(type(activo))   # <class 'bool'>
print()

# ------------------------------------------------------------
# 3️⃣ Reglas para nombrar variables
# Correctas:
mi_variable = 10
nombre_usuario = "Lucia"
_total_precio = 50.5
# Incorrectas (NO LAS EJECUTES):
# 2nombre = "Error"
# mi-variable = 10
# nombre usuario = "Error"

# ------------------------------------------------------------
# 4️⃣ Ejemplos de tipos de datos más comunes

# int - número entero
numero_entero = 25

# float - número decimal
numero_decimal = 3.14

# str - texto
mensaje = "Hola, Python!"

# bool - valor lógico
es_verdadero = False

# list - lista (colección ordenada y modificable)
frutas = ["manzana", "banana", "pera"]

# tuple - tupla (colección ordenada pero inmutable)
colores = ("rojo", "verde", "azul")

# dict - diccionario (clave: valor)
persona = {"nombre": "Usain", "edad": 35, "pais": "Argentina"}



# set - conjunto (sin orden y sin duplicados)
numeros = {1, 2, 3, 3, 4, 4, 5}

# Mostramos todo:
print("Ejemplos de tipos de datos:")
print(numero_entero)
print(numero_decimal)
print(mensaje)
print(es_verdadero)
print(frutas)
print(colores)
print(persona)
print(numeros)
print()

# ------------------------------------------------------------
# 5️⃣ Casting - Conversión de tipos de datos

x = "25"        # str
y = int(x)      # convierte a entero
z = float(x)    # convierte a decimal
texto = str(100)  # convierte un número a texto

print("Conversión de tipos:")
print(f"x = {x} ({type(x)})")
print(f"y = {y} ({type(y)})")
print(f"z = {z} ({type(z)})")
print(f"texto = {texto} ({type(texto)})")
print()

# ------------------------------------------------------------
# 6️⃣ Operaciones entre variables

a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Operaciones con números:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print()

# ------------------------------------------------------------
# 7️⃣ Mostrar valores combinando texto y variables
print(f"Mi nombre es {nombre}, tengo {edad} años y mido {altura} metros.")
print(f"¿Estoy activo en el sistema? {activo}")
print(f"Mis frutas favoritas son: {frutas}")
print(f"Mi color favorito es: {colores[0]}")
print(f"Vivo en {persona['pais']}")
print()

# ============================================================
