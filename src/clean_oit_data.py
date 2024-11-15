def clean_oit_data(df, output_dir="../data/processed/"):
    """
    Limpia un DataFrame con datos del OIT y lo guarda en un archivo CSV.

    Los datos originales fueron extraídos de la plataforma ILOSTAT Data Explorer
    (https://rshiny.ilo.org/dataexplorer). Esta función
    limpia y transforma los datos para su posterior análisis.

    Args:
        df (pd.DataFrame): DataFrame con datos del OIT.
        output_dir (str, optional): Directorio de salida para los archivos CSV. Defaults to "../data/processed/".
    """

    # Filtra los datos por Venezuela
    df = df[df['ref_area.label'].str.contains('Venezuela')]

    # Selecciona el nombre del indicador
    indicator_label = df['indicator.label'].unique()[0].lower().replace('/', '-').replace(' ', '_')

    # Selecciona las columnas relevantes
    df = df[['sex.label', 'classif1.label', 'classif2.label', 'time', 'obs_value']]

    # Limpia y renombra las columnas ambiguas
    for col in ['sex.label', 'classif1.label', 'classif2.label']:
        # Crear un DataFrame separado para cada clave única
        df_temp = df[[col]].copy()
        df_temp[col] = df_temp[col].str.split(':').str[0]
        df_temp = df_temp.groupby(col).size().reset_index(name='count')

        # Crear nuevas columnas en el DataFrame original
        for index, row in df_temp.iterrows():
            df[row[col]] = df[col].apply(lambda x: x.split(':')[1] if x.startswith(row[col] + ':') else '')

        # Eliminar la columna original
        df.drop(col, axis=1, inplace=True)

    # Limpia el nombre del indicador y crea el nombre del archivo
    filename = f"{output_dir}cleanned_{indicator_label}.csv"

    # Guarda el DataFrame
    df.to_csv(filename, index=False)
