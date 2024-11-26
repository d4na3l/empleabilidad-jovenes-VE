import pandas as pd
import glob
import os

# Definir el directorio donde están los archivos CSV
csv_file = '/home/soporte/Escritorio/empleabilidad-jovenes-VE/data/data_WF'
output_dir = '/home/soporte/Escritorio/empleabilidad-jovenes-VE/data/processed_wf'

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Obtener todos los archivos CSV en la carpeta data_WF
all_files = glob.glob(os.path.join(csv_file, "*.csv"))

############Filtro de palabras
ref = pd.read_csv('/home/soporte/Escritorio/empleabilidad-jovenes-VE/data/filter/filtro.csv')
filter = ref['PALABRAS'].to_list()
filtro_regex = '|'.join(filter)

#############

# Crear un diccionario para almacenar los DataFrames, donde la clave es el nombre del archivo
dataframes = {}
# Lista para almacenar los nombres de los archivos
file_names = []

# Funcion para leer cada archivo y crear un DataFrame independiente
def procesar_archivo(file, filtro_regex, dataframes, file_names):
    try:

        # Leer archivo con encabezado en la línea 2 (header=1)
        df = pd.read_csv(file, delimiter=',', header=1, on_bad_lines='skip')
        
        # Reemplazar NaN por una cadena vacía si es necesario
        df = df.fillna('')
        
        # Realizar filtrado
        if 'IDENTIFICADOR' in df.columns:
            df_filtrado = df[df['IDENTIFICADOR'].str.contains(filtro_regex, case=False, na=False)]
        else:
            print(f"Advertencia: La columna 'IDENTIFICADOR' no existe en {file}.")
            return
        
        # Obtener el nombre del archivo sin la ruta y sin extensión
        filename = os.path.splitext(os.path.basename(file))[0]
        
        # Guardar el DataFrame en el diccionario con el nombre del archivo como clave
        dataframes[filename] = df
        file_names.append(filename)
        
        # Guardar ek Dataframe en un archivo csv
        output_path = os.path.join(output_dir, f"{filename}_filtrado.csv")
        df_filtrado.to_csv(output_path, index=False)
        print(f"Archivo filtrado guardado en: {output_path}")
        
    except Exception as e:
        print(f"Error al procesar el archivo {file}: {e}")
        
def mostrar_dataframe(nombre_archivo):
    if nombre_archivo in dataframes:
        print(f"\nDataFrame para {nombre_archivo}:")
        print(dataframes[nombre_archivo])
    else:
        print(f"El archivo '{nombre_archivo}' no se encontró en el directorio.")
        
# Función para generar tablas pivote a partir de un archivo CSV
def generar_tabla_pivote(file):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(file)
        
        # Verificar si el DataFrame no está vacío
        if df.empty:
            print(f"El archivo {file} no contiene datos.")
            return None
        
        # Generar una tabla pivote (puedes personalizar esto según tus necesidades)
        # En este ejemplo, asumo que quieres hacer una tabla pivote usando 'IDENTIFICADOR'
        # como índice y los valores semestrales como columnas. Ajusta esto según los datos reales.
        if 'IDENTIFICADOR' in df.columns:
            tabla_pivote = pd.pivot_table(
                df, 
                index='IDENTIFICADOR', 
                aggfunc='sum',  # Función de agregación, ajusta según sea necesario
                fill_value=0  # Reemplazar NaN con 0
            )
            return tabla_pivote
        else:
            print(f"El archivo {file} no contiene la columna 'IDENTIFICADOR'.")
            return None

    except Exception as e:
        print(f"Error al generar tabla pivote para el archivo {file}: {e}")
        return None

# Función para mostrar la lista de archivos CSV filtrados y generar una tabla pivote
def seleccionar_archivo_para_tabla_pivote():
    # Mostrar todos los archivos CSV filtrados disponibles
    print("Archivos CSV filtrados disponibles:")
    archivos_procesados = [f for f in os.listdir(output_dir) if f.endswith('_filtrado.csv')]
    
    if not archivos_procesados:
        print("No hay archivos CSV filtrados disponibles.")
        return
    
    # Listar archivos con números para selección
    for i, archivo in enumerate(archivos_procesados):
        print(f"{i + 1}. {archivo}")
    
    # Pedir al usuario que seleccione un archivo por número
    try:
        seleccion = int(input("\nSelecciona el número del archivo que quieres ver como tabla pivote ;) "))
        if 1 <= seleccion <= len(archivos_procesados):
            archivo_seleccionado = archivos_procesados[seleccion - 1]
            archivo_path = os.path.join(output_dir, archivo_seleccionado)
            
            # Generar y mostrar la tabla pivote
            tabla_pivote = generar_tabla_pivote(archivo_path)
            if tabla_pivote is not None:
                print(f"\nTabla pivote para {archivo_seleccionado}:")
                print(tabla_pivote)
            else:
                print("No se pudo generar la tabla pivote.")
        else:
            print("Selección fuera de rango. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

# Ejemplo de uso de la función de selección
for file in all_files:
    procesar_archivo(file, filtro_regex, dataframes, file_names)
    seleccionar_archivo_para_tabla_pivote()        