# ============================================================
# La función print() en Python
# ============================================================


# 1️⃣ Tu primer print: mostrar texto en pantalla
print("Hola, mundo!")  # Muestra el texto dentro de las comillas

# ------------------------------------------------------------
# 2️⃣ Mostrar varios valores separados por comas
print("Hola", "soy", "Usain")  # Por defecto separa con espacios

# ------------------------------------------------------------
# 3️⃣ Mostrar variables con print
nombre = 'Usain'
edad = 35
print("Mi nombre es", nombre, "y tengo", edad, "años.")  # Combina texto y variables

# ------------------------------------------------------------
# 4️⃣ Usando f-strings (forma moderna y más legible)
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Inserta variables dentro del texto

# También se pueden usar expresiones dentro de las llaves
print(f"El doble de mi edad es {edad * 2}")

# ------------------------------------------------------------
# 5️⃣ Mostrar resultados de operaciones
print("La suma de 3 + 5 es:", 3 + 5)
a = 10
b = 2
print(f"{a} dividido por {b} es {a / b}")  # División usando f-string

# ------------------------------------------------------------
# 6️⃣ Parámetro sep: cambia el separador entre los elementos
print("Python", "es", "genial", sep="-")  # Une las palabras con guiones
print("2025", "10", "12", sep="/")        # Formato de fecha

# ------------------------------------------------------------
# 7️⃣ Parámetro end: evita el salto de línea al final
print("Hola", end=" ")  # No salta de línea
print("Mundo")          # Se imprime en la misma línea

# Otro ejemplo con un bucle
for i in range(5):
    print(i, end=", ")  # Imprime los números separados por comas

print()  # Agrega un salto de línea final para limpiar la salida

# ------------------------------------------------------------
# 8️⃣ Saltos de línea con \n
print("Hola\nMundo")  # \n genera un salto de línea

# ------------------------------------------------------------
# 9️⃣ Imprimir una línea vacía
print()  # Solo imprime un salto de línea

# ------------------------------------------------------------
# 10️⃣ Ejemplo completo con varios tipos de salida
print("=== EJEMPLO COMPLETO ===")
ciudad = "Buenos Aires"
pais = "Argentina"
print(f"Vivo en {ciudad}, {pais}.")
print("Temperaturas registradas:", 20, 25, 27, sep=" | ")

# ------------------------------------------------------------

