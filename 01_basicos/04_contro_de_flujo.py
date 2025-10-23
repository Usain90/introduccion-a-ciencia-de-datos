# ============================================================
# Control de flujo en Python (código práctico)
# ============================================================

print("=== 1) if / elif / else ===")
edad = 20
if edad >= 18:
    print("Sos mayor de edad")
elif 13 <= edad < 18:
    print("Sos adolescente")
else:
    print("Sos menor")

# Combinando condiciones
usuario_activo = True
tiene_permiso = False
if usuario_activo and tiene_permiso:
    print("Acceso concedido")
else:
    print("Acceso denegado")
print()

# ------------------------------------------------------------

print("=== 2) match / case (Python 3.10+) ===")
# Elegir acción por comando
comando = "guardar"

match comando:
    case "abrir":
        print("Abrir archivo")
    case "guardar":
        print("Guardar archivo")
    case "salir":
        print("Salir del programa")
    case _:
        print("Comando no reconocido")

# Pattern matching con tuplas y guardas
punto = (3, 0)
match punto:
    case (0, 0):
        print("Origen")
    case (x, 0):
        print(f"Sobre eje X, x={x}")
    case (0, y):
        print(f"Sobre eje Y, y={y}")
    case (x, y) if x == y:
        print(f"Sobre la diagonal x=y, x={x}")
    case (x, y):
        print(f"Punto cualquiera: ({x}, {y})")
print()

# ------------------------------------------------------------

print("=== 3) for: range, enumerate, zip ===")

# range(inicio, fin, paso)
for i in range(1, 6):
    print("i:", i, end=" | ")
print("\n")

# enumerate: índice y valor
materias = ["Python", "Datos", "IA"]
for idx, nombre in enumerate(materias, start=2):
    print(f"{idx}. {nombre}")
print()

# zip: iteración en paralelo
alumnos = ["Ana", "Luis", "Mika"]
notas = [9, 7, 10]
for alumno, nota in zip(alumnos, notas):
    print(f"{alumno}: {nota}")
print()

# ------------------------------------------------------------

print("=== 4) while ===")
# Contador simple con condición de salida
contador = 3
while contador > 0:
    print("Cuenta atrás:", contador)
    contador -= 1


# Ejemplo de validación (simulado)
entrada = "ok"
intentos = 0
while entrada != "ok" and intentos < 3:
    
    intentos += 1
print("Fin del while (simulado)\n")

# ------------------------------------------------------------

print("=== 5) break / continue / pass ===")

# break: salir del bucle al encontrar un objetivo
for n in range(1, 10):
    if n % 7 == 0:
        print("Encontré múltiplo de 7:", n)
        break  # termina el for
    # else: seguir buscando

# continue: saltar iteración cuando la condición se cumple
for n in range(1, 6):
    if n == 3:
        continue  # salta imprimir el 3
    print("n (sin 3):", n)

# pass: placeholder (no hace nada)
for _ in range(2):
    pass  # completar lógica más tarde
print()

# ------------------------------------------------------------

print("=== 6) else en bucles ===")
# El else se ejecuta si el bucle NO terminó por 'break'
for n in [2, 4, 6, 8]:
    if n == 5:
        print("Encontré un 5")
        break
else:
    print("Recorrí todo y no había un 5")  # se ejecuta

# Con while
k = 0
while k < 3:
    k += 1
    # if k == 2: break
else:
    print("while terminó sin break")
print()

# ------------------------------------------------------------

print("=== 7) Buenas prácticas y ejemplos útiles ===")

# a) Encadenamiento de comparaciones
x = 7
if 0 < x < 10:  # más claro que: x > 0 and x < 10
    print("x está entre 1 y 9")

# b) Guardar la condición en una variable para legibilidad
nombre = "Usain"
es_valido = (len(nombre) >= 3) and nombre.isalpha()
if es_valido:
    print("Nombre válido")

# c) Evitar while True infinitos (salida clara)
intentos = 0
while True:
    intentos += 1
    if intentos >= 2:
        print("Salgo del while True de forma controlada")
        break
print()

# ------------------------------------------------------------

print("=== 8) Mini-retos para practicar ===")
# Reto A: Pedí (simulado) una nota de 0 a 100 y clasificá:
# 90-100: Excelente, 75-89: Muy bien, 60-74: Aprobado, <60: Reprobado
nota = 83
match nota:
    case n if 90 <= n <= 100:
        print("Excelente")
    case n if 75 <= n <= 89:
        print("Muy bien")
    case n if 60 <= n <= 74:
        print("Aprobado")
    case _:
        print("Reprobado")

# Reto B: Recorre una lista y salteá cadenas vacías con continue
nombres = ["Ana", "", "Luis", "  ", "Mika"]
for n in nombres:
    if n.strip() == "":
        continue
    print("Válido:", n)

# Reto C: Usá else en for para verificar si un número primo fue encontrado
numero = 11
for d in range(2, int(numero**0.5) + 1):
    if numero % d == 0:
        print(numero, "NO es primo (divisible por", d, ")")
        break
else:
    print(numero, "es primo")
# ============================================================
# FIN DEL CAPÍTULO 6
# ============================================================
