import pandas as pd
import glob
import os

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

# Leer cada archivo y crear un DataFrame independiente
for file in all_files:
    try:
        # Leer archivo con encabezado en la línea 2 (header=1)
        df = pd.read_csv(file, delimiter=',', header=1)
        
        # Reemplazar NaN por una cadena vacía si es necesario
        df = df.fillna('')
        
        #############Filtro de palabras
        filtrado = df[df['IDENTIFICADOR'].str.contains(filtro_regex, case=False, na=False)]

        # filtrado = df.fillna("")

            #############

        # Obtener el nombre del archivo sin la ruta y sin extensión
        filename = os.path.splitext(os.path.basename(file))[0]
        
        # Guardar el DataFrame en el diccionario con el nombre del archivo como clave
        dataframes[filename] = df
        
    except Exception as e:
        print(f"Error al procesar el archivo {file}: {e}")

# Ejemplo de cómo acceder a cada DataFrame individualmente
for nombre_archivo, dataframe in dataframes.items():
    print(f"DataFrame para {nombre_archivo}:")
    print(dataframe)
    print("\n" + "-"*50 + "\n")