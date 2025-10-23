# ============================================================
# Colecciones en Python (código práctico)
# ============================================================

print("=== 1) STRINGS (str) ===")
s = "  Python para principiantes  "


print("Original:", repr(s))
print("len(s):", len(s))
print("slice s[2:8]:", s[2:8])
print("strip():", s.strip())
print("lower():", s.lower())
print("upper():", s.upper())
print("replace('para','para PRO'): ", s.replace("para", "para PRO"))
print("'para' in s:", "para" in s)
print("'Py' in s (case-sensitive):", "Py" in s)
print("split():", s.split())      # divide por espacios
print("'|'.join(['A','B','C']):", "|".join(["A","B","C"]))
print()

# ------------------------------------------------------------

print("=== 2) LISTAS (list) ===")
nums = [5, 2, 9, 2]
print("Lista inicial:", nums)

# Mutabilidad (agregar/quitar)
nums.append(7)             # agrega al final
nums.extend([1, 3])        # agrega varios

nums

nums.insert(5, 99)         # inserta en índice 1
print("Después de append/extend/insert:", nums)

nums.remove(2)             # quita primera ocurrencia de 2
p = nums.pop()             # quita y devuelve último
print("Después de remove(2) y pop():", nums, "| pop devolvió:", p)

print("count(2):", nums.count(2))
print("index(99):", nums.index(99))
nums.sort()                # ordena in-place
print("sort() asc:", nums)
nums.reverse()             # revierte in-place
print("reverse():", nums)

# Slicing y copia superficial
copia = nums[:]
copia
print("copia via [:]:", copia, "| misma ref?:", copia is nums)
print()

# ------------------------------------------------------------

print("=== 3) TUPLAS (tuple) ===")
t = (10, 20, 30)
print("Tupla t:", t)
a, b, c = t   # desempaquetado
print("Desempaquetado:", a, b, c)
# t[0] = 99  # ❌ Error: inmutable
print()

# ------------------------------------------------------------

print("=== 4) DICCIONARIOS (dict) ===")
persona = {"nombre": "Usain", "edad": 30}
print("Dict inicial:", persona)

# Acceso y actualización
print(persona["edad"])
print("get('pais','N/A'):", persona.get("pais", "N/A"))

persona["pais"] = "Argentina"     # agregar/actualizar
persona.update({"rol": "DS", "edad": 31})
print("Tras update:", persona)

# Quitar
valor = persona.pop("rol")
print("pop('rol') →", valor, "| dict:", persona)

# Vistas
print("keys():", list(persona.keys()))
print("values():", list(persona.values()))
print("items():", list(persona.items()))

# Iteración con desempaquetado
for k, v in persona.items():
    print(f"{k} -> {v}")
print()

# ------------------------------------------------------------

print("=== 5) SETS (set) ===")
s1 = {1, 2, 2, 3}  # duplicados se eliminan
s2 = {3, 4, 5}
print("s1:", s1)
print("s2:", s2)

# Operaciones de conjuntos
print("Unión (|):", s1 | s2)
print("Intersección (&):", s1 & s2)
print("Diferencia (s1 - s2):", s1 - s2)
print("Simétrica (^):", s1 ^ s2)

# Mutación
s1.add(10)
s1.discard(2)   # no falla si no está
print("Tras add/discard:", s1)
print()

# ------------------------------------------------------------

print("=== 6) SLICING (strings/listas/tuplas) ===")
seq = ["a", "b", "c", "d", "e", "f"]
print("seq:", seq)
print("seq[:3]:", seq[:3])
print("seq[2:5]:", seq[2:5])
print("seq[::2]:", seq[::2])   # paso 2
print("seq[::-1]:", seq[::-1]) # reverso
print()

# ------------------------------------------------------------

print("=== 7) COPIAS: shallow vs deep ===")
import copy

anidada = [[1, 2], [3, 4]]
shallow = list(anidada)          # o anidada.copy() / anidada[:]
deep = copy.deepcopy(anidada)

anidada[0][0] = 99
print("Original:", anidada)
print("Shallow:", shallow)        # se ve afectada (comparte sublistas)
print("Deep:", deep)              # NO se afecta
print()

# ------------------------------------------------------------

print("=== 8) ITERACIÓN / enumerate / zip / sorted ===")
letras = ["x", "y", "z"]
for i, ch in enumerate(letras, start=1):
    print(f"{i}) {ch}")

nombres = ["Ana", "Mika", "Luis"]
notas = [10, 9, 7]
for n, nota in zip(nombres, notas):
    print(f"{n}: {nota}")

print("sorted(notas):", sorted(notas))
print("sorted(nombres, reverse=True):", sorted(nombres, reverse=True))
print()

# ------------------------------------------------------------

print("=== 9) COMPREHENSIONS ===")
# List comprehension
cuadrados = [x*x for x in range(1, 6)]
pares = [x for x in range(10) if x % 2 == 0]
print("cuadrados:", cuadrados)
print("pares:", pares)

# Dict comprehension
calificaciones = {al: no for al, no in zip(nombres, notas)}
print("dict comp:", calificaciones)

# Set comprehension
letras_unicas = {ch for ch in "programacion" if ch.isalpha()}
print("set comp:", letras_unicas)
print()

# ------------------------------------------------------------

print("=== 10) Mini-retos ===")
# Reto A: Dada una frase, construir una lista de palabras en minúscula sin signos
frase = "¡Python, para Principiantes! Es genial."
tokens = [p.strip("¡!?,.;:").lower() for p in frase.split()]
print("tokens:", tokens)

# Reto B: De una lista con repetidos, obtener set de únicos y dict {valor: conteo}
data = ["a", "b", "a", "c", "b", "a"]
unicos = set(data)
conteo = {x: data.count(x) for x in unicos}
print("únicos:", unicos)
print("conteo:", conteo)

# Reto C: Dado un dict de precios, crear uno con IVA 21% aplicado
precios = {"pan": 100, "leche": 250, "queso": 1200}
precios_con_iva = {k: round(v * 1.21, 2) for k, v in precios.items()}
print("precios con IVA:", precios_con_iva)

# ============================================================
