import os
import pandas as pd
import matplotlib.pyplot as plt


def procesar_archivo(nombre_archivo, filtro_regex, input_dir, output_dir):
    """
    Procesa un archivo CSV aplicando un filtro y guarda el resultado en otro archivo CSV.
    Si el archivo ya ha sido generado previamente, lo carga y muestra.

    Args:
        nombre_archivo (str): Nombre del archivo (sin extensión) que deseas procesar.
        filtro_regex (str): Expresión regular para filtrar filas.
        input_dir (str): Directorio de entrada donde se encuentra el archivo CSV.
        output_dir (str): Directorio donde se guardará el archivo filtrado.

    Returns:
        pd.DataFrame: DataFrame generado o cargado.
    """
    # Configuración para visualizar todas las columnas en la misma línea
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.width', 1000)

    try:
        # Construir rutas completas
        file = os.path.join(input_dir, f"{nombre_archivo}.csv")
        output_path = os.path.join(output_dir, f"{nombre_archivo}_filtrado.csv")
        
        # Verificar si el archivo filtrado ya existe
        if os.path.exists(output_path):
            print(f"El archivo filtrado ya existe. Cargando desde: {output_path}")
            df_filtrado = pd.read_csv(output_path)
            print("DataFrame generado previamente:")
            print(df_filtrado)
            return df_filtrado
        
        # Leer el archivo CSV con encabezado en la línea 2 (header=1)
        df = pd.read_csv(file, delimiter=',', header=1, on_bad_lines='skip')

        # Reemplazar NaN por cadena vacía (si es necesario)
        df = df.fillna('')

        # Verificar si la columna 'IDENTIFICADOR' existe y aplicar el filtro
        if 'IDENTIFICADOR' not in df.columns:
            raise KeyError(f"La columna 'IDENTIFICADOR' no existe en el archivo {file}.")

        df_filtrado = df[df['IDENTIFICADOR'].str.contains(filtro_regex, case=False, na=False)]

        # Mostrar el DataFrame generado
        print("DataFrame generado:")
        print(df_filtrado)

        # Crear directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Guardar el DataFrame filtrado
        df_filtrado.to_csv(output_path, index=False)
        print(f"Archivo filtrado guardado en: {output_path}")
        return df_filtrado

    except Exception as e:
        print(f"Error al procesar el archivo {nombre_archivo}: {e}")
        
def guardar_dataframe(dataframe, output_dir, nombre_archivo):
    """
    Guarda un DataFrame en un archivo CSV en la ruta especificada. 
    Si el archivo ya existe, lo carga y muestra en lugar de sobrescribirlo.

    Args:
        dataframe (pd.DataFrame): El DataFrame que se desea guardar.
        output_dir (str): Directorio donde se guardará el archivo.
        nombre_archivo (str): Nombre del archivo (sin extensión).

    Returns:
        pd.DataFrame: DataFrame cargado (si ya existía el archivo) o recién guardado.
    """
    try:
        # Construir la ruta completa del archivo
        output_path = os.path.join(output_dir, f"{nombre_archivo}.csv")
        
        # Verificar si el archivo ya existe
        if os.path.exists(output_path):
            print(f"El archivo ya existe. Cargando desde: {output_path}")
            df_existente = pd.read_csv(output_path)
            print("DataFrame existente:")
            print(df_existente)
            return df_existente
        
        # Crear el directorio si no existe
        os.makedirs(output_dir, exist_ok=True)
        
        # Guardar el DataFrame en un archivo CSV
        dataframe.to_csv(output_path, index=False)
        print(f"Archivo guardado en: {output_path}")
        return dataframe

    except Exception as e:
        print(f"Error al guardar el DataFrame: {e}")
        
import os
import pandas as pd

def procesar_archivo(nombre_archivo, filtro_regex, input_dir, output_dir):
    """
    Procesa un archivo CSV aplicando un filtro, utiliza el título de la primera línea como título del archivo
    y lo agrega como una línea separada antes de los datos tanto en el DataFrame como en el CSV generado.

    Args:
        nombre_archivo (str): Nombre del archivo (sin extensión) que deseas procesar.
        filtro_regex (str): Expresión regular para filtrar filas.
        input_dir (str): Directorio de entrada donde se encuentra el archivo CSV.
        output_dir (str): Directorio donde se guardará el archivo filtrado.

    Returns:
        str: El título extraído.
        pd.DataFrame: DataFrame generado o cargado.
    """
    # Configuración para visualizar todas las columnas en la misma línea
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.width', 1000)

    try:
        # Construir rutas completas
        file = os.path.join(input_dir, f"{nombre_archivo}.csv")
        output_path = os.path.join(output_dir, f"{nombre_archivo}_filtrado.csv")
        
        # Verificar si el archivo filtrado ya existe
        if os.path.exists(output_path):
            print(f"El archivo filtrado ya existe. Cargando desde: {output_path}")
            with open(output_path, 'r') as f:
                titulo = f.readline().strip()  # Leer el título de la primera línea del archivo generado
            df_filtrado = pd.read_csv(output_path, skiprows=1)
            print(f"Título del DataFrame:\n{titulo}\n")
            print("DataFrame generado previamente:")
            print(df_filtrado)
            return titulo, df_filtrado
        
        # Leer el título (línea 0) del archivo original
        with open(file, 'r') as f:
            titulo = f.readline().strip()
        
        # Leer el archivo CSV con encabezado en la línea 2 (header=1)
        df = pd.read_csv(file, delimiter=',', header=1, on_bad_lines='skip')

        # Reemplazar NaN por cadena vacía (si es necesario)
        df = df.fillna('')

        # Verificar si la columna 'IDENTIFICADOR' existe y aplicar el filtro
        if 'IDENTIFICADOR' not in df.columns:
            raise KeyError(f"La columna 'IDENTIFICADOR' no existe en el archivo {file}.")

        df_filtrado = df[df['IDENTIFICADOR'].str.contains(filtro_regex, case=False, na=False)]

        # # Mostrar el título y el DataFrame generado
        print(f"\n{titulo}\n")
        # print("DataFrame generado con filtro:")
        print(df_filtrado)

        # Crear directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Escribir el título y el DataFrame en el archivo CSV
        with open(output_path, 'w') as f:
            f.write(titulo + '\n')  # Escribir el título como primera línea
            df_filtrado.to_csv(f, index=False, header=True)

        print(f"Archivo filtrado con título guardado en: {output_path}")
        return titulo, df_filtrado

    except Exception as e:
        print(f"Error al procesar el archivo {nombre_archivo}: {e}")