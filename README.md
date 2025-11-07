# Sistema de Gestión de Países – Programación I
### Trabajo Práctico Integrador – Tecnicatura Universitaria en Programación – UTN FRM

Este proyecto forma parte del Trabajo Práctico Integrador de la materia Programación I.  
El sistema permite gestionar información de países usando Python y un archivo CSV como base de datos.  
Incluye búsquedas, filtros, ordenamientos, estadísticas y una tabla formateada con alineación automática.

---

##  Descripción del programa

El programa es un sistema interactivo que opera sobre un dataset de países.  
Permite realizar las siguientes acciones:

###  Buscar países por nombre
La búsqueda es parcial (ej: “ar” → Argentina, Nigeria).

###  Filtrar países
- Por continente  
- Por rango de población  
- Por rango de superficie  

###  Ordenar países
- Por nombre (A→Z y Z→A)  
- Por población (asc/desc)  
- Por superficie (asc/desc)  

###  Mostrar estadísticas
- País con mayor población  
- País con menor población  
- Promedio de población  
- Promedio de superficie  
- Cantidad de países por continente  

###  Mostrar tabla completa
Con columnas alineadas y números formateados.

###  Manejo de archivos
Si el archivo CSV no existe, el sistema lo crea automáticamente.

---

##  Requisitos

- Python 3.8 o superior  
- No requiere librerías externas  

---

##  Instrucciones de uso

1. Hacer clic en el botón verde **"Code"** de este repositorio.  
2. Seleccionar **"Download ZIP"**.  
3. Descomprimir el ZIP en cualquier carpeta.  
4. Abrir la carpeta del proyecto.  
5. Verificar que estén los archivos:
   - `tpi.py`
   - `paises.csv`
   - carpeta `capturas/`
6. Abrir una terminal en la carpeta:
   - **Windows:** Shift + clic derecho → "Abrir ventana PowerShell aquí"
   - **Linux/Mac:** abrir terminal y navegar a la carpeta
7. Ejecutar el programa:
     python tpi.py
   
 # ✅ Ejemplos de entradas y salidas

### 🔎 Ejemplo 1 – Búsqueda por nombre

**Entrada:**

argentina


**Salida:**


Argentina 45.376.763 2.780.400 América


---

###  Ejemplo 2 – Filtro por continente

**Entrada:**


Europa


**Salida:**


Alemania 83.149.300 357.022 Europa
Francia 68.042.591 551.695 Europa


---

###  Ejemplo 3 – Filtro por población

**Entrada:**


mínimo: 20000000
máximo: 100000000


**Salida:**


Australia 26.068.792
Argentina 45.376.763
Sudáfrica 60.414.495
Francia 68.042.591
Alemania 83.149.300


---

###  Ejemplo 4 – Estadísticas

**Salida:**


Mayor población: India (1.428.627.663)
Menor población: Australia (26.068.792)
Promedio de población: 236.942.811
Promedio de superficie: 3.928.565
Países por continente:
América: 3
Europa: 2
Asia: 2
África: 2
Oceanía: 1


---

##  Estructura del proyecto



TPI-Programacion-Paises/
│ tpi.py
│ paises.csv
│ README.md
│
└── capturas/
captura_menu.png
captura_busqueda.png
captura_filtros.png
captura_ordenamiento.png
captura_estadisticas.png


---

##  Participación de los integrantes

**Alumnos:** *Joaquin Moran y Paul Paiva*

- Desarrollo completo del código  
- Diseño del menú y funciones  
- Validación de datos y manejo de errores  
- Elaboración del informe del TPI  
- Capturas del funcionamiento  
- Grabación del video de presentación  

---

##  Licencia
Proyecto académico – Libre para uso educativo.
