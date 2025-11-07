from __future__ import annotations
import csv
import os
from typing import List, Dict, Optional, Tuple

CSV_PATH = "paises.csv"
CSV_FIELDS = ["nombre", "poblacion", "superficie", "continente"]

# ---------------------------------------------------------------------
# UTILIDADES DE ARCHIVOS Y VALIDACIÓN
# ---------------------------------------------------------------------

def create_default_csv(path: str = CSV_PATH) -> None:
    """Crea un CSV base si no existe."""
    sample = [
        {"nombre": "Argentina", "poblacion": "45376763", "superficie": "2780400", "continente": "América"},
        {"nombre": "Japón", "poblacion": "125800000", "superficie": "377975", "continente": "Asia"},
        {"nombre": "Brasil", "poblacion": "213993437", "superficie": "8515767", "continente": "América"},
        {"nombre": "Alemania", "poblacion": "83149300", "superficie": "357022", "continente": "Europa"},
        {"nombre": "Nigeria", "poblacion": "223804632", "superficie": "923768", "continente": "África"},
        {"nombre": "Australia", "poblacion": "26068792", "superficie": "7692024", "continente": "Oceanía"},
        {"nombre": "Canadá", "poblacion": "38929902", "superficie": "9984670", "continente": "América"},
        {"nombre": "India", "poblacion": "1428627663", "superficie": "3287263", "continente": "Asia"},
        {"nombre": "Francia", "poblacion": "68042591", "superficie": "551695", "continente": "Europa"},
        {"nombre": "Sudáfrica", "poblacion": "60414495", "superficie": "1221037", "continente": "África"},
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in sample:
            writer.writerow(row)


def ensure_csv_exists(path: str = CSV_PATH) -> None:
    if not os.path.exists(path):
        print("[INFO] CSV no encontrado. Creando archivo base...")
        create_default_csv(path)


def validate_and_cast_row(raw: Dict[str, str]) -> Optional[Dict[str, object]]:
    try:
        nombre = raw.get("nombre", "").strip()
        continente = raw.get("continente", "").strip()

        if not nombre or not continente:
            return None

        poblacion = int(raw["poblacion"])
        superficie = int(raw["superficie"])

        if poblacion < 0 or superficie <= 0:
            return None

        return {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
    except Exception:
        return None


def load_countries(path: str = CSV_PATH) -> List[Dict[str, object]]:
    items = []
    invalid = 0

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for raw in reader:
            row = validate_and_cast_row(raw)
            if row is None:
                invalid += 1
            else:
                items.append(row)

    if invalid > 0:
        print(f"[AVISO] Se ignoraron {invalid} filas inválidas.")
    return items

# ---------------------------------------------------------------------
# BUSQUEDA Y FILTROS
# ---------------------------------------------------------------------

def search_by_name(items, query: str):
    q = query.lower()
    return [p for p in items if q in p["nombre"].lower()]


def filter_by_continent(items, cont: str):
    c = cont.lower()
    return [p for p in items if p["continente"].lower() == c]


def filter_by_range(items, key: str, mn: Optional[int], mx: Optional[int]):
    def ok(v):
        if mn is not None and v < mn:
            return False
        if mx is not None and v > mx:
            return False
        return True
    return [p for p in items if ok(p[key])]

# ---------------------------------------------------------------------
# ORDENAMIENTOS
# ---------------------------------------------------------------------

def sort_countries(items, key, descending=False):
    if key == "nombre":
        return sorted(items, key=lambda x: x["nombre"].lower(), reverse=descending)
    return sorted(items, key=lambda x: x[key], reverse=descending)

# ---------------------------------------------------------------------
# ESTADÍSTICAS
# ---------------------------------------------------------------------

def max_min_population(items):
    return (
        max(items, key=lambda x: x["poblacion"]),
        min(items, key=lambda x: x["poblacion"])
    )


def average(items, key):
    return sum(x[key] for x in items) / len(items)


def count_by_continent(items):
    conts = {}
    for p in items:
        c = p["continente"]
        conts[c] = conts.get(c, 0) + 1
    return conts

# ---------------------------------------------------------------------
# PRESENTACIÓN
# ---------------------------------------------------------------------

def format_int(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def print_table(items: List[Dict[str, object]]):
    if not items:
        print("No hay datos para mostrar.")
        return

    cols = ["Nombre", "Población", "Superficie (km²)", "Continente"]

    width_nombre = max(len(p["nombre"]) for p in items)
    width_nombre = max(width_nombre, len(cols[0]))

    width_pob = max(len(format_int(p["poblacion"])) for p in items)
    width_pob = max(width_pob, len(cols[1]))

    width_sup = max(len(format_int(p["superficie"])) for p in items)
    width_sup = max(width_sup, len(cols[2]))

    width_cont = max(len(p["continente"]) for p in items)
    width_cont = max(width_cont, len(cols[3]))

    header = (
        f"{cols[0]:<{width_nombre}}  "
        f"{cols[1]:>{width_pob}}  "
        f"{cols[2]:>{width_sup}}  "
        f"{cols[3]:<{width_cont}}"
    )

    print(header)
    print("-" * len(header))

    for p in items:
        print(
            f"{p['nombre']:<{width_nombre}}  "
            f"{format_int(p['poblacion']):>{width_pob}}  "
            f"{format_int(p['superficie']):>{width_sup}}  "
            f"{p['continente']:<{width_cont}}"
        )

# ---------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------

def ask_int_or_blank(prompt: str) -> Optional[int]:
    txt = input(prompt).strip()
    if txt == "":
        return None
    try:
        n = int(txt)
        if n < 0:
            print("Debe ser >= 0.")
            return ask_int_or_blank(prompt)
        return n
    except ValueError:
        print("Debe ser un número.")
        return ask_int_or_blank(prompt)

# ---------------------------------------------------------------------
# SUBMENUS
# ---------------------------------------------------------------------

def submenu_filtros(items):
    print("\n--- FILTROS ---")
    print("a) Por continente")
    print("b) Por rango de población")
    print("c) Por rango de superficie")
    print("x) Volver")
    op = input("Elegí una opción: ").strip().lower()

    if op == "a":
        c = input("Continente: ").strip()
        res = filter_by_continent(items, c)
        if not res:
            print("Sin resultados.")
            return None
        return sort_countries(res, "nombre")

    elif op == "b":
        mn = ask_int_or_blank("Población mínima: ")
        mx = ask_int_or_blank("Población máxima: ")
        res = filter_by_range(items, "poblacion", mn, mx)
        if not res:
            print("Sin resultados.")
            return None
        return sort_countries(res, "poblacion")

    elif op == "c":
        mn = ask_int_or_blank("Superficie mínima: ")
        mx = ask_int_or_blank("Superficie máxima: ")
        res = filter_by_range(items, "superficie", mn, mx)
        if not res:
            print("Sin resultados.")
            return None
        return sort_countries(res, "superficie")

    else:
        return None


def submenu_ordenamientos(items):
    print("\n--- ORDENAMIENTOS ---")
    print("a) Nombre A→Z")
    print("b) Nombre Z→A")
    print("c) Población asc")
    print("d) Población desc")
    print("e) Superficie asc")
    print("f) Superficie desc")
    print("x) Volver")
    op = input("Opción: ").strip().lower()

    if op == "a": return sort_countries(items, "nombre", False)
    if op == "b": return sort_countries(items, "nombre", True)
    if op == "c": return sort_countries(items, "poblacion", False)
    if op == "d": return sort_countries(items, "poblacion", True)
    if op == "e": return sort_countries(items, "superficie", False)
    if op == "f": return sort_countries(items, "superficie", True)
    return None


def mostrar_estadisticas(items):
    maxi, mini = max_min_population(items)
    prom_p = average(items, "poblacion")
    prom_s = average(items, "superficie")
    conts = count_by_continent(items)

    print("\n--- ESTADÍSTICAS ---")
    print(f"Mayor población: {maxi['nombre']} ({format_int(maxi['poblacion'])})")
    print(f"Menor población: {mini['nombre']} ({format_int(mini['poblacion'])})")
    print(f"Promedio de población: {format_int(int(prom_p))}")
    print(f"Promedio de superficie: {format_int(int(prom_s))}")
    print("Países por continente:")
    for c, cant in conts.items():
        print(f"  {c}: {cant}")

# ---------------------------------------------------------------------
# MENU
#   PRINCIPAL
# ---------------------------------------------------------------------

def menu_principal():
    ensure_csv_exists()
    paises = load_countries()

    while True:
        print("\n=== GESTIÓN DE PAÍSES ===")
        print("1) Buscar país")
        print("2) Filtrar países")
        print("3) Ordenar países")
        print("4) Estadísticas")
        print("5) Ver todos")
        print("0) Salir")
        op = input("Opción: ").strip()

        if op == "1":
            q = input("Nombre o parte del nombre: ")
            res = search_by_name(paises, q)
            print_table(res)

        elif op == "2":
            res = submenu_filtros(paises)
            if res: print_table(res)

        elif op == "3":
            res = submenu_ordenamientos(paises)
            if res: print_table(res)

        elif op == "4":
            mostrar_estadisticas(paises)

        elif op == "5":
            print_table(sort_countries(paises, "nombre"))

        elif op == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido.")
