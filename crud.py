
def search_by_name(items,q):
    q=q.lower()
    return [p for p in items if q in p["nombre"].lower()]

def filter_by_continent(items,c):
    c=c.lower()
    return [p for p in items if p["continente"].lower()==c]

def filter_by_range(items,key,mn,mx):
    return [p for p in items if p[key]>=mn and p[key]<=mx]

def sort_countries(items,key,desc=False):
    if key=="nombre":
        return sorted(items,key=lambda x:x["nombre"].lower(),reverse=desc)
    return sorted(items,key=lambda x:x[key],reverse=desc)

def create_country(nombre,poblacion,superficie,continente):
    return {"nombre":nombre,"poblacion":poblacion,"superficie":superficie,"continente":continente}

def update_country_by_name(items,nombre,np,ns,nc):
    for p in items:
        if p["nombre"].lower()==nombre.lower():
            p["poblacion"]=np
            p["superficie"]=ns
            p["continente"]=nc
            return True
    return False

def delete_country_by_name(items,nombre):
    for i,p in enumerate(items):
        if p["nombre"].lower()==nombre.lower():
            items.pop(i)
            return True
    return False
