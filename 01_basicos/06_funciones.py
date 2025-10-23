# ============================================================
# Funciones en Python (código práctico)
# ============================================================

import math
from typing import Iterable, Callable, Any, Dict, List, Tuple

print("=== 1) Definición, llamada y return ===")
def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"

print(saludar("Usain"))  # Hola, Usain!
print()

# ------------------------------------------------------------

print("=== 2) Parámetros: posicionales, keyword y por defecto ===")
def potencia(base: float, exponente: float = 2) -> float:
    """Eleva 'base' a 'exponente' (por defecto 2)."""
    return base ** exponente

print(potencia(5))              # 25 (por defecto exponente=2)
print(potencia(base=2, exponente=8))  # 256
print()

# ⚠️ Evitar valores mutables como default
def acumular(valor, acumulador=None):
    """Acumula 'valor' en una lista nueva si no se provee."""
    if acumulador is None:
        acumulador = []
    acumulador.append(valor)
    return acumulador

print(acumular(1))  # [1]
print(acumular(2))  # [2] (listas distintas, correcto)
print()

# ------------------------------------------------------------

print("=== 3) *args y **kwargs (variádicos) ===")
def resumen_pedido(*items: str, **extras: Any) -> str:
    """
    *items: argumentos posicionales variables (tupla)
    **extras: argumentos nombrados variables (dict)
    """
    base = ", ".join(items) if items else "sin items"
    if extras:
        kv = ", ".join(f"{k}={v}" for k, v in extras.items())
        return f"Pedido: {base} | Extras: {kv}"
    return f"Pedido: {base}"

print(resumen_pedido("pizza", "empanadas", bebida="agua", postre="helado"))
print()

# ------------------------------------------------------------

print("=== 4) Posicional-solo y Sólo-keyword (3.8+) ===")
def escalar(x, y, /, *, factor=1.0):
    """
    x, y: deben pasarse posicionalmente (antes de '/')
    factor: debe pasarse como keyword (después de '*')
    """
    return (x * factor, y * factor)

print(escalar(2, 3, factor=0.5))  # (1.0, 1.5)
# escalar(x=2, y=3, factor=0.5)  # ❌ Error: x,y posicional-solo
print()

# ------------------------------------------------------------

print("=== 5) Scope (LEGB), global y nonlocal ===")
PI = 3.14159  # global

def ejemplo_scope():
    mensaje = "local"

    def inner():
        nonlocal mensaje  # modifica el 'mensaje' de ejemplo_scope (enclosing)
        global PI         # referencia/modifica variable global
        mensaje = "modificado en inner"
        PI_local = PI     # leer global es ok
        return mensaje, PI_local

    out = inner()
    return mensaje, out

print("scope:", ejemplo_scope())
print("PI global:", PI)  # (no modificamos PI en este ejemplo)
print()

# ------------------------------------------------------------

print("=== 6) Docstrings y help() ===")
def area_circulo(r: float) -> float:
    """Devuelve el área de un círculo de radio r."""
    return math.pi * r * r

# help(area_circulo)  # descomentar para ver doc en consola
print(f"Área radio 3: {area_circulo(3):.2f}")
print()

# ------------------------------------------------------------

print("=== 7) Anotaciones de tipos (type hints) ===")
def sumar(a: int, b: int) -> int:
    return a + b

def filtrar_positivos(xs: Iterable[int]) -> list[int]:
    return [x for x in xs if x > 0]

print("sumar:", sumar(2, 3))
print("positivos:", filtrar_positivos([-2, 0, 5, 7, -1]))
print()

# ------------------------------------------------------------

print("=== 8) lambda, closures y funciones de orden superior ===")
# lambda
doble = lambda n: n * 2  # funciones cortas y expresivas
print("doble(6):", doble(6))

# closure: recordar un valor del entorno
def multiplicador(factor: int) -> Callable[[int], int]:
    """Devuelve una función que multiplica por 'factor'."""
    def aplicar(n: int) -> int:
        return n * factor  # 'factor' queda "recordado"
    return aplicar

por3 = multiplicador(3)
print("por3(10):", por3(10))  # 30

# map, filter, sorted(key=...)
nums = [5, -2, 10, 1]
print("map(doble):", list(map(doble, nums)))
print("filter positivos:", list(filter(lambda x: x > 0, nums)))
palabras = ["Python", "ia", "datos", "modelo"]
print("sorted por longitud:", sorted(palabras, key=len))
print()

# ------------------------------------------------------------

print("=== 9) Recursión (ejemplo: factorial) ===")
def factorial(n: int) -> int:
    """Calcula n! recursivamente. Requiere n >= 0."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n in (0, 1):    # caso base
        return 1
    return n * factorial(n - 1)  # progreso hacia el caso base

print("factorial(5):", factorial(5))  # 120
print()

# ------------------------------------------------------------

print("=== 10) Patrones útiles y buenas prácticas ===")
# a) Devolver múltiples valores (tupla)
def estadisticas(xs: Iterable[float]) -> Tuple[float, float]:
    """Devuelve (mínimo, máximo)."""
    xs = list(xs)
    return (min(xs), max(xs))

print("min,max:", estadisticas([10, 3, 7, 21]))

# b) Funciones puras vs con efectos (print/IO). Preferir puras para testear.
def neto(precio: float, iva: float = 0.21) -> float:
    return round(precio * (1 + iva), 2)

print("neto(100):", neto(100))

# c) Manejo simple de errores dentro de función
def dividir_seguro(a: float, b: float) -> float | None:
    """Divide a/b; si b=0 devuelve None en lugar de lanzar error."""
    if b == 0:
        return None
    return a / b

print("dividir_seguro(10, 2):", dividir_seguro(10, 2))
print("dividir_seguro(10, 0):", dividir_seguro(10, 0))


# ============================================================
