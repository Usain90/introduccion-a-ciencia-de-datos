# ============================================================
# Operadores en Python (código práctico)
# ============================================================

print("=== 1) Operadores Aritméticos ===")
x, y = 10, 3
# Suma, resta, multiplicación, división "real"
print("Suma:", x + y)              # 13
print("Resta:", x - y)             # 7
print("Multiplicación:", x * y)    # 30
print("División /:", x / y)        # 3.333...

# División entera (floor) y módulo
print("División entera //:", x // y)  # 3
print("Módulo %:", x % y)             # 1

# Potencia
print("Potencia **:", x ** y)         # 1000

# ⚠️ Nota: // hace "floor", ojo con negativos
print("(-7)//3:", (-7) // 3)          # -3 (no -2)
print("(-7)%3:", (-7) % 3)            # 2 (se cumple: a == (a//b)*b + (a%b) )


print()

# ------------------------------------------------------------

print("=== 2) Operadores de Comparación ===")
a, b = 5, 5
c = 8

print("a == b:", a == b)   # True
print("a != c:", a != c)   # True
print("a > c:", a > c)     # False
print("a < c:", a < c)     # True
print("a >= b:", a >= b)   # True
print("a <= b:", a <= b)   # True

# Chaining (encadenamiento) de comparaciones
print("5 < 8 < 12:", 5 < 8 < 12)  # True (equivale a (5 < 8) and (8 < 12))
print()

# ------------------------------------------------------------

print("=== 3) Operadores Lógicos ===")
t, f = True, False
edad = 20

# and, or, not
print("True and False:", t and f)         
print("True or False:", t or f)           
print("not True:", not t)                 

# Combinando condiciones
print("18 <= edad < 30:", 18 <= edad < 30)  # True

# Cortocircuito (short-circuit): si la primera es False en AND, no evalúa lo demás
def funcion_costosa():
    print("→ Se evaluó funcion_costosa()")
    return True

print("False and funcion_costosa():", False and funcion_costosa())  # No llama a la función
print("True and funcion_costosa():", True and funcion_costosa())    # Llama a la función
print()

# ------------------------------------------------------------

print("=== 4) Operadores de Asignación ===")
n = 10     # asignación simple
n += 2     # n = n + 2
n -= 3     # n = n - 3
n *= 4     # n = n * 4
n /= 3     # n = n / 3  → float
print("n tras +=, -=, *=, /=:", n)

# Más asignaciones compuestas
m = 17
m //= 3    # división entera
m %= 5     # módulo
m **= 2    # potencia
print("m tras //=, %=, **=:", m)
print()

# ------------------------------------------------------------

print("=== 5) Operadores de Pertenencia (in / not in) ===")
frutas = ["manzana", "pera", "banana"]
print("'pera' in frutas:", "pera" in frutas)           # True
print("'kiwi' not in frutas:", "kiwi" not in frutas)   # True

# En strings verifica subcadenas
texto = "python es genial"
print("'thon' in texto:", "thon" in texto)   # True
print("'Py' in texto:", "Py" in texto)       # False (case-sensitive)
print()

# En diccionarios, 'in' revisa claves
persona = {"nombre": "Usain", "edad": 30}
print("'nombre' in persona:", "nombre" in persona)     # True (clave)
print("'Usain' in persona:", "Usain" in persona)       # False (valor)
print("'Usain' in persona.values():", "Usain" in persona.values())  # True
print()

# ------------------------------------------------------------

print("=== 6) Operadores de Identidad (is / is not) ===")
lista_a = [1, 2, 3]
lista_b = lista_a      # misma referencia
lista_c = [1, 2, 3]    # distinta lista, mismo contenido

print("lista_a is lista_b:", lista_a is lista_b)   # True (mismo objeto)
print("lista_a is lista_c:", lista_a is lista_c)   # False (objetos distintos)
print("lista_a == lista_c:", lista_a == lista_c)   # True (mismo contenido)

# Caso típico con pequeños enteros y strings (interning puede hacer 'is' True a veces,
# pero NO lo uses para comparar igualdad de valores; usá ==)
x1 = 256
x2 = 256
print("x1 == x2:", x1 == x2)   # True
print("x1 is x2:", x1 is x2)   # (implementación dependiente; no relies en esto)
print()

# ------------------------------------------------------------

print("=== 7) Precedencia y Paréntesis ===")
# Precedencia (de mayor a menor): **, *, /, //, %, +, -, comparaciones, not, and, or
# Usá paréntesis para dejar clara la intención
expr1 = 3 + 2 * 5          
expr2 = (3 + 2) * 5        
expr3 = 2 ** 3 ** 2        # 2 ** (3 ** 2) = 2 ** 9 = 512 (potencia es derecha-asociativa)
print("3 + 2 * 5:", expr1)
print("(3 + 2) * 5:", expr2)
print("2 ** 3 ** 2:", expr3)
print()



# ------------------------------------------------------------

# EX A: Dado un entero n, imprimir:
# - si es múltiplo de 3 y 5 (FizzBuzz)
# - si es solo múltiplo de 3 (Fizz)
# - si es solo múltiplo de 5 (Buzz)
# - en otro caso, imprimir el número


n = 30
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


# ==========================================================
a = 'usain'
b = 'usain'
print(a == b)