
from utils import *
from crud import *
from stats import *

CSV_PATH = "paises.csv"

def menu():
    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1) Ver todos")
    print("2) Buscar")
    print("3) Filtrar")
    print("4) Ordenar")
    print("5) Estadísticas")
    print("6) Agregar")
    print("7) Editar")
    print("8) Eliminar")
    print("9) Guardar")
    print("0) Salir")

def submenu_filtros():
    print("\n--- FILTROS ---")
    print("a) Continente")
    print("b) Rango población")
    print("c) Rango superficie")
    print("x) Volver")
    return input("Opción: ").lower().strip()

def submenu_orden():
    print("\n--- ORDENAR ---")
    print("a) Nombre A-Z")
    print("b) Nombre Z-A")
    print("c) Población ↑")
    print("d) Población ↓")
    print("e) Superficie ↑")
    print("f) Superficie ↓")
    print("x) Volver")
    return input("Opción: ").lower().strip()

def main():
    ensure_csv_exists(CSV_PATH)
    paises = load_countries(CSV_PATH)
    dirty = False

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            print_table(sort_countries(paises,"nombre"))

        elif op == "2":
            q = pedir_texto("Buscar nombre: ")
            print_table(search_by_name(paises,q))

        elif op == "3":
            f = submenu_filtros()
            if f == "a":
                c = pedir_texto("Continente: ")
                print_table(filter_by_continent(paises,c))
            elif f == "b":
                mn = pedir_entero_min("mín: ",0)
                mx = pedir_entero_min("máx: ",mn)
                print_table(filter_by_range(paises,"poblacion",mn,mx))
            elif f == "c":
                mn = pedir_entero_min("mín: ",1)
                mx = pedir_entero_min("máx: ",mn)
                print_table(filter_by_range(paises,"superficie",mn,mx))

        elif op == "4":
            o = submenu_orden()
            if o=="a": print_table(sort_countries(paises,"nombre"))
            if o=="b": print_table(sort_countries(paises,"nombre",True))
            if o=="c": print_table(sort_countries(paises,"poblacion"))
            if o=="d": print_table(sort_countries(paises,"poblacion",True))
            if o=="e": print_table(sort_countries(paises,"superficie"))
            if o=="f": print_table(sort_countries(paises,"superficie",True))

        elif op == "5":
            mostrar_estadisticas(paises)
            if pedir_opcion("Ver avanzadas? [s/n]: ",["s","n"])=="s":
                n = pedir_entero_rango("Top N (1-10): ",1,10)
                mostrar_estadisticas_avanzadas(paises,n)

        elif op == "6":
            nuevo = create_country(
                pedir_texto("Nombre: "),
                pedir_entero_min("Población: ",0),
                pedir_entero_min("Superficie: ",1),
                pedir_texto("Continente: ")
            )
            paises.append(nuevo); dirty=True; print("Agregado.")

        elif op == "7":
            nom = pedir_texto("Editar país: ")
            ok = update_country_by_name(
                paises, nom,
                pedir_entero_min("Nueva población: ",0),
                pedir_entero_min("Nueva superficie: ",1),
                pedir_texto("Nuevo continente: ")
            )
            print("Editado." if ok else "No existe."); dirty |= ok

        elif op == "8":
            nom = pedir_texto("Eliminar país: ")
            ok = delete_country_by_name(paises,nom)
            print("Eliminado." if ok else "No existe."); dirty |= ok

        elif op == "9":
            save_countries(CSV_PATH,paises)
            print("Guardado."); dirty=False

        elif op == "0":
            if dirty and confirmar("Guardar antes de salir? [s/n]: "):
                save_countries(CSV_PATH,paises)
            print("Chau!")
            break

if __name__ == "__main__":
    main()
