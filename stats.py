
from utils import format_int

def max_min_population(items):
    return max(items,key=lambda x:x["poblacion"]), min(items,key=lambda x:x["poblacion"])

def average(items,key):
    return sum(x[key] for x in items)/len(items)

def count_by_continent(items):
    d={}
    for p in items:
        c=p["continente"]
        d[c]=d.get(c,0)+1
    return d

def mostrar_estadisticas(items):
    mx,mn = max_min_population(items)
    print("\n--- ESTADÍSTICAS ---")
    print("Mayor población:",mx["nombre"],format_int(mx["poblacion"]))
    print("Menor población:",mn["nombre"],format_int(mn["poblacion"]))
    print("Promedio población:",format_int(int(average(items,"poblacion"))))
    print("Promedio superficie:",format_int(int(average(items,"superficie"))))
    print("Por continente:")
    for c,n in count_by_continent(items).items():
        print(" ",c,n)

def densidad(p):
    return p["poblacion"]/p["superficie"]

def top_n_by_population(items,n):
    return sorted(items,key=lambda x:x["poblacion"],reverse=True)[:n]

def mostrar_estadisticas_avanzadas(items,n):
    print("\n--- ESTADÍSTICAS AVANZADAS ---")
    dens = sorted(items,key=densidad,reverse=True)[:n]
    print("Top densidad:")
    for p in dens:
        print(" ",p["nombre"],f"{densidad(p):.2f}")
    print("Top población:")
    for p in top_n_by_population(items,n):
        print(" ",p["nombre"],format_int(p["poblacion"]))
