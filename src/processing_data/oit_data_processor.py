import pandas as pd
import numpy as np
import re
import warnings
from util.util_rutas import obtener_ruta_absoluta


def load_data(filepath, rename_columns=None, columns_to_keep=None):
    """
    Load a CSV file with optional renaming and column filtering.
    """
    try:
        df = pd.read_csv(filepath)
        if rename_columns:
            valid_renames = {k: v for k, v in rename_columns.items() if k in df.columns}
            df.rename(columns=valid_renames, inplace=True)

        if columns_to_keep:
            df = df[[col for col in columns_to_keep if col in df.columns]]

        return df

    except Exception as e:
        warnings.warn(f"Error loading CSV: {e}")
        return pd.DataFrame()

def remove_totals(df, columns):
    """
    Remove rows where specified columns contain the word 'Total'.
    """
    valid_columns = [col for col in columns if col in df.columns and df[col].notna().any()]
    if not valid_columns:
        return df.reset_index(drop=True)

    mask = ~pd.concat([df[col].str.contains('Total', na=False) for col in valid_columns], axis=1).any(axis=1)
    return df[mask].reset_index(drop=True)

def extract_age(age_str):
    """
    Extract age ranges or single ages from a string.
    """
    if pd.isna(age_str) or not isinstance(age_str, str):
        return None

    # Remover prefijos innecesarios
    if ':' in age_str:
        age_str = age_str.split(':', 1)[-1].strip()

    # Definir patrones para identificar edades
    patterns = [r'(\d+)-(\d+)', r'(\d+)\+', r'(\d+)']
    for pattern in patterns:
        match = re.search(pattern, age_str)
        if match:
            if '-' in age_str:
                return int(match.group(1)), int(match.group(2))
            elif '+' in age_str:
                return int(match.group(1)), None
            else:
                return int(match.group(1)), int(match.group(1))

    # Si no coincide con ningún patrón
    return None

def filter_age_range(df, min_allowed=15, max_allowed=30):
    """
    Filter DataFrame rows based on the extracted age range.

    Args:
        df (pd.DataFrame): Input DataFrame with 'age_extracted' column.
        min_allowed (int): Minimum age allowed for inclusion.
        max_allowed (int): Maximum age allowed for inclusion.

    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    def is_within_range(age_range):
        if pd.isna(age_range):
            return False
        min_age, max_age = age_range

        # Si solo hay límite inferior (None en el segundo valor)
        if max_age is None:
            return min_allowed <= min_age <= max_allowed

        # Si ambos límites están definidos, verificar que ambos caigan dentro del rango permitido
        if min_age >= min_allowed and max_age <= max_allowed:
            return True

        return False
    # Aplicar el filtro
    return df[df['age_extracted'].apply(is_within_range)]

def remove_parentheses_content(df, column):
    """
    Remove all content within parentheses in the specified column, including the parentheses.
    """
    if column in df.columns:
        df[column] = df[column].astype(str).replace(r'\(.*?\)', '', regex=True).str.strip()
    return df


def preprocess_data(df):
    # Extraer rango de edades
    if 'classif1' in df.columns:
        df['age_extracted'] = df['classif1'].apply(extract_age)

    if 'classif2' in df.columns:
        df = remove_parentheses_content(df, 'classif2')

    # Convertir valores numéricos en 'obs_value'
    if 'obs_value' in df.columns:
        df['obs_value'] = pd.to_numeric(df['obs_value'], errors='coerce')

    return df.dropna(subset=['obs_value']).reset_index(drop=True)

def fill_missing_values(df, group_cols=None):
    """
    Fill missing values in a DataFrame based on similar rows.
    """
    if not group_cols or not all(col in df.columns for col in group_cols):
        warnings.warn("Some group columns are missing. Skipping filling.")
        return df

    def find_closest(row):
        if not pd.isna(row['obs_value']):
            return row['obs_value']

        # Ajustar para manejar columnas opcionales
        conditions = [(df['sex'] == row['sex']), (df['classif1'] == row['classif1'])]
        if 'classif2' in df.columns and 'classif2' in row:
            conditions.append(df['classif2'] == row['classif2'])

        similar = df[np.logical_and.reduce(conditions) & (~df['obs_value'].isna())]
        if not similar.empty:
            closest_idx = (similar['time'].astype(int) - int(row['time'])).abs().idxmin()
            return similar.loc[closest_idx, 'obs_value']

        return np.nan

    df['obs_value'] = df.apply(find_closest, axis=1)
    return df


def analyze_dataset(df):
    """
    Provide an analysis of the dataset structure.
    """
    return {
        'total_rows': len(df),
        'column_completeness': {
            col: {
                'null_count': df[col].isnull().sum(),
                'null_percentage': df[col].isnull().mean() * 100
            } for col in df.columns
        },
        'unique_values': {col: df[col].unique().tolist() for col in df.columns if df[col].nunique() < 50}
    }


def export_dataframe(df, filename, filepath=obtener_ruta_absoluta('data/processed')):
    """
    Export the DataFrame to a CSV file.
    """
    full_path = f"{filepath}/{filename}"
    df.to_csv(full_path, index=False)

def process_pipeline(filepath, rename_columns=None, columns_to_keep=None, min_allowed=15, max_allowed=30):
    """
    Full pipeline for data processing and cleaning.

    Args:
        filepath (str): Path to the input file.
        rename_columns (dict): Optional column renaming map.
        columns_to_keep (list): Optional columns to retain.
        min_allowed (int): Minimum age allowed for inclusion.
        max_allowed (int): Maximum age allowed for inclusion.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    # Cargar datos
    df = load_data(filepath, rename_columns, columns_to_keep)

    # Remover filas con Totales (sólo columnas que existan)
    df = remove_totals(df, [col for col in ['sex', 'classif1', 'classif2'] if col in df.columns])

    # Preprocesar datos
    df = preprocess_data(df)

    # Filtrar por rango de edad
    df = filter_age_range(df, min_allowed=min_allowed, max_allowed=max_allowed)

    # Llenar valores faltantes (ignorar columnas que no estén presentes)
    group_cols = [col for col in ['sex', 'classif1', 'classif2'] if col in df.columns]
    df = fill_missing_values(df, group_cols)
    # Exportar resultados
    export_dataframe(df, 'cleanned_'+filepath.split('/')[-1])
    return df


