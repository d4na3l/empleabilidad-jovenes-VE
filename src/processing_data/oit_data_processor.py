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


def fill_missing_values(df, is_pivot=False, group_cols=None):
    """
    Fill missing values in a DataFrame or Pivot Table.

    Args:
        df (pd.DataFrame): DataFrame to fill.
        is_pivot (bool): If True, applies interpolation on pivot table.
        group_cols (list, optional): Columns to group by for filling in non-pivot tables.

    Returns:
        pd.DataFrame: DataFrame with filled values.
    """
    if is_pivot:
        # Interpolación en tablas dinámicas (pivot tables)
        return df.interpolate(method='linear', axis=0, limit_direction='both')

    if not group_cols:
        raise ValueError("`group_cols` must be provided for non-pivot DataFrames.")

    # Verifica si las columnas existen en el DataFrame
    missing_cols = [col for col in group_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"The following columns are missing in the DataFrame: {missing_cols}")

    # Step 1: Rellenar valores faltantes con la media del grupo
    df['obs_value'] = df.groupby(group_cols)['obs_value'].transform(lambda x: x.fillna(x.mean()))

    # Step 2: Rellenar valores faltantes restantes usando el valor más cercano
    def find_closest(row):
        if not pd.isna(row['obs_value']):
            return row['obs_value']
        similar = df[
            (df['sex'] == row['sex']) &
            (df['classif1'] == row['classif1']) &
            (df['classif2'] == row['classif2']) &
            (~df['obs_value'].isna())
        ]
        if not similar.empty:
            return similar.loc[(similar['time'] - row['time']).abs().idxmin(), 'obs_value']
        return np.nan

    df['obs_value'] = df.apply(find_closest, axis=1)
    return df



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
