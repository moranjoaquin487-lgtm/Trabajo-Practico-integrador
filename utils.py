
import csv,os

CSV_FIELDS=["nombre","poblacion","superficie","continente"]

def create_default_csv(path):
    pass

def ensure_csv_exists(path):
    if not os.path.exists(path):
        print("[INFO] creando CSV base...")
        with open(path,"w",newline="",encoding="utf-8") as f:
            w=csv.writer(f); w.writerow(CSV_FIELDS)

def validate_and_cast_row(r):
    try:
        return {
            "nombre":r["nombre"].strip(),
            "poblacion":int(r["poblacion"]),
            "superficie":int(r["superficie"]),
            "continente":r["continente"].strip()
        }
    except:
        return None

def load_countries(path):
    items=[]
    with open(path,encoding="utf-8") as f:
        rd=csv.DictReader(f)
        for r in rd:
            row=validate_and_cast_row(r)
            if row: items.append(row)
    return items

def save_countries(path,items):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(CSV_FIELDS)
        for p in items:
            w.writerow([p["nombre"],p["poblacion"],p["superficie"],p["continente"]])

def format_int(n): return f"{n:,}".replace(",", ".")

def print_table(items):
    if not items:
        print("Sin datos."); return
    print(f"{'Nombre':<15}{'Población':>15}{'Superficie':>15}{'Continente':>15}")
    print("-"*60)
    for p in items:
        print(f"{p['nombre']:<15}{format_int(p['poblacion']):>15}{format_int(p['superficie']):>15}{p['continente']:>15}")

def pedir_texto(msg):
    t=input(msg).strip()
    while not t:
        print("No vacío."); t=input(msg).strip()
    return t

def pedir_entero_min(msg,mn):
    while True:
        try:
            n=int(input(msg))
            if n>=mn: return n
            print("Muy chico.")
        except: print("Número inválido.")

def pedir_entero_rango(msg,a,b):
    while True:
        try:
            n=int(input(msg))
            if a<=n<=b: return n
            print("Fuera de rango.")
        except: print("Inválido.")

def pedir_opcion(msg,ops):
    o=input(msg).lower().strip()
    while o not in ops:
        o=input(msg).lower().strip()
    return o

def confirmar(msg):
    return pedir_opcion(msg,["s","n"])=="s"
