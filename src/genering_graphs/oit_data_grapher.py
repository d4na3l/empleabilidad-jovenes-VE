import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt


def plot_pie_chart(df, group_col, value_col, title="Pie Chart"):
    """
    Create a pie chart showing the proportion of a value column grouped by another column.

    Args:
        df (pd.DataFrame): Input DataFrame.
        group_col (str): Column name to group data by (e.g., 'sex').
        value_col (str): Column name for values (e.g., 'obs_value').
        title (str): Title for the chart.

    Returns:
        None: Displays the chart.
    """
    # Aggregate data by the group column
    data = df.groupby(group_col)[value_col].sum()

    # Create pie chart
    plt.figure(figsize=(8, 8))
    data.plot.pie(autopct='%1.1f%%', startangle=90, legend=True)

    # Add title
    plt.title(title)
    plt.ylabel('')  # Remove y-label for better visualization
    plt.tight_layout()
    plt.show()

def plot_grouped_bar_chart(df, group_col, x_col, y_col, title):
    """
    Create a grouped bar chart with filtering for the top 5 categories of x_col
    if there are too many categories. Also, adjust the label orientation to avoid overlap.

    Args:
        df (pd.DataFrame): Input DataFrame.
        group_col (str): Column name to group data by (e.g., 'classif1').
        x_col (str): Column name for x-axis values (e.g., 'classif2').
        y_col (str): Column name for y-axis values (e.g., 'obs_value').
        title (str): Title for the chart.

    Returns:
        None: Displays the chart.
    """

    # Verificar si hay datos en la columna x_col (sin valores nulos)
    if df[x_col].isnull().all():
        x_col = 'sex'  # Cambiar a 'sex' si 'classif2' no tiene datos válidos

    # Pivotar el DataFrame para preparar el gráfico de barras agrupadas
    pivot_data = df.pivot_table(values=y_col, index=x_col, columns=group_col, aggfunc='sum')

    # Filtrar por las 5 categorías más representativas de x_col basadas en la cantidad de datos en y_col
    if pivot_data.shape[0] > 3:  # Verificar que haya más de 5 categorías en el eje x
        # Contar la cantidad total de datos por categoría en x_col
        top_x_categories = df.groupby(x_col)[y_col].sum().nlargest(3).index  # Las 5 categorías más frecuentes
        pivot_data = pivot_data.loc[top_x_categories]  # Filtrar por las 5 categorías más representativas

    # Graficar gráfico de barras agrupadas
    ax = pivot_data.plot(kind='bar', figsize=(12, 6))

    # Ajustar etiquetas del eje x para evitar superposiciones
    plt.title(title, fontdict=None, loc='center', pad=None)
    plt.xlabel('Parametros de observación')
    plt.ylabel('Valores observados')

    # Ajustar las etiquetas de las columnas (de abajo hacia arriba a izquierda a derecha)
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')  # Rotar etiquetas y alinearlas a la derecha
    plt.legend(title='Criterio de medición', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # Asegurar que todo se vea bien ajustado
    plt.show()


def plot_line_chart(df, time_col, classif2_col, y_col, title):
    """
    Create a line chart to show the progression over time with respect to classif2.
    If there are more than 5 categories in classif2, select the 5 most prominent.

    Args:
        df (pd.DataFrame): Input DataFrame.
        time_col (str): Column name for the time values (e.g., 'year').
        classif2_col (str): Column name for the categories to group by (e.g., 'classif2').
        y_col (str): Column name for the y-axis values (e.g., 'obs_value').
        title (str): Title for the chart.

    Returns:
        None: Displays the chart, or nothing if no data exists for classif2.
    """

    # Verificar si hay datos en la columna classif2
    if df[classif2_col].isnull().all():
        print("No data for classif2. No chart will be displayed.")
        return  # Si no hay datos para classif2, no hacer nada

    # Filtrar por las 5 categorías más representativas de classif2 basadas en la cantidad de datos en y_col
    if df[classif2_col].nunique() > 5:  # Verificar que haya más de 5 categorías en classif2
        # Contar la cantidad total de datos por categoría en classif2
        top_categories = df.groupby(classif2_col)[y_col].sum().nlargest(5).index  # Las 5 categorías más relevantes
        df = df[df[classif2_col].isin(top_categories)]  # Filtrar las filas que corresponden a esas categorías

    # Agrupar por el tiempo y classif2 para sumar los valores de y_col
    grouped_data = df.groupby([time_col, classif2_col])[y_col].sum().unstack(fill_value=0)

    # Graficar gráfico lineal
    ax = grouped_data.plot(kind='line', figsize=(12, 6), marker='o')

    # Ajustar el título y las etiquetas
    plt.title(title, fontdict=None, loc='center', pad=None)
    plt.xlabel('Año')
    plt.ylabel('Valores observados')

    # Configurar el eje X para que muestre todos los años
    plt.xticks(grouped_data.index, rotation=45, ha='right')  # Mostrar todos los años y girar las etiquetas

    # Ajustar la leyenda
    plt.legend(title='Parametros de observación', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  # Asegurar que todo se vea bien ajustado
    plt.show()
