import pandas as pd
import glob
import os
from tabulate import tabulate

# Definir el directorio donde están los archivos CSV
csv_file = '/home/soporte/Escritorio/empleabilidad-jovenes-VE/data/data_WF'

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

# Leer cada archivo y crear un DataFrame independiente
for file in all_files:
    try:
        # Leer archivo con encabezado en la línea 2 (header=1)
        df = pd.read_csv(file, delimiter=',', header=1, on_bad_lines='skip')
        
        # Reemplazar NaN por una cadena vacía si es necesario
        df = df.fillna('')
        
        # Filtro de palabras
        df = df[df['IDENTIFICADOR'].str.contains(filtro_regex, case=False, na=False)]

        # Obtener el nombre del archivo sin la ruta y sin extensión
        filename = os.path.splitext(os.path.basename(file))[0]
        
        # Guardar el DataFrame en el diccionario con el nombre del archivo como clave
        dataframes[filename] = df
        file_names.append(filename)
        
    except Exception as e:
        print(f"Error al procesar el archivo {file}: {e}")

# Función para mostrar la lista de archivos y seleccionar uno
# Función para mostrar la lista de archivos y seleccionar uno
# def seleccionar_archivo():
#     # Mostrar todos los nombres de archivo con un número asignado
#     print("Archivos disponibles en 'empleabilidad-jovenes-VE/data/data_WF':")
#     for i, name in enumerate(file_names):
#         print(f"{i + 1}. {name}")
    
#     # Pedir al usuario que seleccione un archivo por número
#     try:
#         seleccion = int(input("\nSelecciona el número del archivo que quieres analizar: "))
#         if 1 <= seleccion <= len(file_names):
#             nombre_archivo = file_names[seleccion - 1]
#             crear_tabla_pivote(nombre_archivo)
#         else:
#             print("Selección fuera de rango. Inténtalo de nuevo.")
#     except ValueError:
#         print("Entrada no válida. Por favor, introduce un número.")

# # Función para crear y mostrar una tabla pivote
# def crear_tabla_pivote(nombre_archivo):
#     df = dataframes[nombre_archivo]
#     print("\nColumnas disponibles para la tabla pivote:")
#     print(list(df.columns))

#     # Pedir al usuario que elija las columnas para la tabla pivote
#     try:
#         index_col = input("\nIntroduce el nombre de la columna que quieres usar como índice (agrupación): ")
#         values_col = input("Introduce el nombre de la columna que quieres sumar o contar: ")
#         aggfunc = input("Introduce la función de agregación (sum, count, mean, etc.): ")

#         # Crear la tabla pivote
#         pivot_table = pd.pivot_table(df, index=index_col, values=values_col, aggfunc=aggfunc)

#         # Mostrar la tabla pivote
#         print("\nTabla Pivote:\n")
#         print(tabulate(pivot_table, headers='keys', tablefmt='fancy_grid'))
#     except KeyError:
#         print("Una de las columnas especificadas no existe. Inténtalo de nuevo.")
#     except Exception as e:
#         print(f"Error al crear la tabla pivote: {e}")

# # Ejemplo de uso de la función de selección
# seleccionar_archivo()
for nombre_archivo, dataframe in dataframes.items():
    print(f"DataFrame para {nombre_archivo}:")
    print(dataframe)
    print("\n" + "-"*50 + "\n")