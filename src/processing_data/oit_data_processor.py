import pandas as pd
import numpy as np

def load_data(filepath, rename_columns=None, columns_to_keep=None):
    """
    Load a CSV file into a DataFrame, optionally renaming columns.

    Args:
        filepath (str): Path to the CSV file.
        rename_columns (dict, optional): Mapping of columns to rename. Defaults to None.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(filepath)
    if rename_columns:
        existing_rename_map = {k: v for k, v in rename_columns.items() if k in df.columns}
        df.rename(columns=existing_rename_map, inplace=True)

    if columns_to_keep:
        df = df[[col for col in columns_to_keep if col in df.columns]]
    return df

def fill_missing_values(df, group_cols=None):
    """
    Fill missing values in a DataFrame by copying values from the closest matching rows.

    Args:
        df (pd.DataFrame): DataFrame to fill.
        group_cols (list): Columns to group by when searching for closest matches.

    Returns:
        pd.DataFrame: DataFrame with missing values filled.
    """
    if not group_cols:
        raise ValueError("`group_cols` must be provided for identifying groups.")

    # Verificar si todas las columnas existen en el DataFrame
    missing_cols = [col for col in group_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"The following columns are missing in the DataFrame: {missing_cols}")

    # Función para encontrar el valor más cercano en el tiempo
    def find_closest(row):
        if not pd.isna(row['obs_value']):
            return row['obs_value']

        # Filtrar registros similares
        similar = df[
            (df['sex'] == row['sex']) &
            (df['classif1'] == row['classif1']) &
            (df['classif2'] == row['classif2']) &
            (~df['obs_value'].isna())  # Solo filas sin NaN en obs_value
        ]

        if not similar.empty:
            # Buscar el registro más cercano en el tiempo
            closest_idx = (similar['time'] - row['time']).abs().idxmin()
            return similar.loc[closest_idx, 'obs_value']

        return np.nan  # Si no se encuentra un valor, dejar como NaN

    # Aplicar la función fila por fila
    df['obs_value'] = df.apply(find_closest, axis=1)
    return df

def remove_totals(df, columns):
    """
    Remove rows where specified columns contain the word 'Total'.

    Args:
        df (pd.DataFrame): DataFrame to clean.
        columns (list): List of columns to check for 'Total'.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    mask = ~pd.concat([df[col].str.contains('Total', na=False) for col in columns], axis=1).any(axis=1)
    return df[mask].reset_index(drop=True)

def create_pivot_table(df, index_col, group_col, value_col='obs_value'):
    """
    Create a pivot table with specified index, columns, and values.

    Args:
        df (pd.DataFrame): DataFrame to pivot.
        index_col (str): Column to use as the index.
        group_col (str): Column to create columns from.
        value_col (str): Column to aggregate values from.

    Returns:
        pd.DataFrame: Pivot table.
    """
    pivot_df = df.pivot_table(index=index_col, columns=group_col, values=value_col)
    pivot_df.fillna(0, inplace=True)
    return pivot_df

def create_total_pivot_table(df, index_col='time', value_col='obs_value', total_cols=None):
    """
    Create a pivot table from rows where specified columns contain 'Total'.

    Args:
        df (pd.DataFrame): DataFrame to process.
        index_col (str): Column to use as the index (e.g., 'time').
        value_col (str): Column containing values to aggregate (e.g., 'obs_value').
        total_cols (list): List of columns to filter for 'Total' values (e.g., ['sex', 'classif1', 'classif2']).

    Returns:
        pd.DataFrame: Combined pivot table with 'Total' values for specified columns.
    """
    if total_cols is None:
        raise ValueError("You must specify the columns to filter for 'Total' values.")

    # List to store intermediate pivot tables
    pivot_tables = []

    for col in total_cols:
        # Filtrar filas donde la columna actual contiene 'Total'
        filtered_df = df[df[col].str.contains('Total', na=False)]

        # Crear la tabla pivote para la columna actual
        pivot = filtered_df.pivot_table(index=index_col, columns=col, values=value_col, aggfunc='sum')

        # Añadir la tabla pivote a la lista
        pivot_tables.append(pivot)

    # Concatenar todas las tablas pivote por columnas
    combined_pivot = pd.concat(pivot_tables, axis=1)

    # Rellenar valores faltantes con 0
    combined_pivot.fillna(0, inplace=True)

    return combined_pivot

def calculate_proportions(df_pivot):
    """
    Calculate row-wise proportions for a pivot table.

    Args:
        df_pivot (pd.DataFrame): Pivot table with numerical values.

    Returns:
        pd.DataFrame: Pivot table with proportions.
    """
    return df_pivot.div(df_pivot.sum(axis=1), axis=0)

def calculate_yearly_change(df_pivot):
    """
    Calculate yearly percentage change for a time-indexed DataFrame.

    Args:
        df_pivot (pd.DataFrame): DataFrame indexed by time.

    Returns:
        pd.DataFrame: DataFrame with yearly percentage change.
    """
    return df_pivot.pct_change().mul(100)

def calculate_correlations(df, numeric_cols=None, categorical_cols=None):
    """
    Calculate correlations for a DataFrame, handling categorical columns.

    Args:
        df (pd.DataFrame): DataFrame to analyze.
        numeric_cols (list, optional): Columns to include directly as numeric.
        categorical_cols (list, optional): Columns to encode as numerical.

    Returns:
        pd.DataFrame: Correlation matrix.
    """
    # Select numeric columns
    numeric_df = df[numeric_cols] if numeric_cols else pd.DataFrame()

    # Encode categorical columns if provided
    if categorical_cols:
        categorical_encoded = pd.get_dummies(df[categorical_cols], drop_first=True)
        numeric_df = pd.concat([numeric_df, categorical_encoded], axis=1)

    # Ensure the DataFrame only contains numeric data
    return numeric_df.corr()



def export_dataframe(df, filename, filepath='../data/processed/'):
    """
    Export a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to export.
        filepath (str): Directory to save the file.
        filename (str): Name of the output file.

    Returns:
        str: Full path to the saved file.
    """
    export_path = f'{filepath}{filename}'
    df.to_csv(export_path, index=False)
