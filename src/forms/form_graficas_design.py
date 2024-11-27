import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
from src.genering_graphs.oit_data_grapher import plot_pie_chart, plot_grouped_bar_chart, plot_line_chart


class FormularioGraficasDesign:
    def __init__(self, parent, df):
        """
        Inicializa el formulario y muestra los gráficos automáticamente al pasar el DataFrame.

        Args:
            parent: Contenedor principal del formulario (Tkinter).
            df: DataFrame con los datos a graficar.
        """
        self.parent = parent  # Recibimos el contenedor principal
        self.cuerpo_principal = parent
        self.df = df  # El DataFrame recibido de la clase anterior

        # Limpia el contenido del cuerpo principal antes de agregar nuevos elementos
        self.limpiar_cuerpo_principal()

        # Crear los tres frames para los gráficos con tamaños específicos
        self.frame_pie = tk.Frame(self.cuerpo_principal, width=600, height=400)  # Gráfico Pie
        self.frame_pie.pack(pady=10, fill='both', expand=True)

        self.frame_barras = tk.Frame(self.cuerpo_principal, width=600, height=400)  # Gráfico Barras
        self.frame_barras.pack(pady=10, fill='both', expand=True)

        self.frame_lineas = tk.Frame(self.cuerpo_principal, width=600, height=400)  # Gráfico Líneas
        self.frame_lineas.pack(pady=10, fill='both', expand=True)

        # Mostrar todos los gráficos automáticamente
        self.mostrar_graficos()

    def limpiar_cuerpo_principal(self):
        """Limpia todos los widgets del cuerpo principal antes de mostrar nuevos gráficos."""
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def obtener_dataframe_actual(self):
        """Obtiene el DataFrame que está siendo utilizado (en este caso, solo hay uno)."""
        return self.df

    def mostrar_graficos(self):
        """
        Muestra los tres gráficos de manera automática:
        - Gráfico de pastel
        - Gráfico de barras agrupadas
        - Gráfico de líneas de evolución temporal
        """
        df = self.obtener_dataframe_actual()

        # Mostrar el gráfico de pastel en su propio frame
        self.mostrar_grafico_pie(self.frame_pie, df)

        # Mostrar el gráfico de barras en su propio frame
        self.mostrar_grafico_barras(self.frame_barras, df)

        # Mostrar el gráfico de líneas en su propio frame
        self.mostrar_grafico_lineas(self.frame_lineas, df)

    def mostrar_grafico_pie(self, frame, df):
        """
        Muestra un gráfico de pastel (pie chart) en el frame indicado.

        Args:
            frame: Frame de Tkinter donde se dibujará el gráfico.
            df: DataFrame con los datos a graficar.
        """
        # Verificar que las columnas necesarias estén presentes
        if 'sex' not in df.columns or 'obs_value' not in df.columns:
            print("Error: Las columnas 'sex' o 'obs_value' no se encuentran en el DataFrame.")
            return  # No continuar si las columnas necesarias no existen

        # Agrupar los datos por 'sex' y sumar 'obs_value' para cada grupo
        data = df.groupby('sex')['obs_value'].sum()

        # Crear el gráfico de pastel
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Para que el gráfico sea circular
        ax.set_title("Distribución por Sexo")

        # Mostrar la figura en el frame
        self.mostrar_figura_en_frame(fig, frame)

    def mostrar_grafico_barras(self, frame, df):
        """
        Muestra un gráfico de barras agrupadas en el frame indicado.

        Args:
            frame: Frame de Tkinter donde se dibujará el gráfico.
            df: DataFrame con los datos a graficar.
        """
        # Verificar que las columnas necesarias estén presentes
        if 'classif2' not in df.columns or 'obs_value' not in df.columns:
            print("Error: Las columnas 'classif2' o 'obs_value' no se encuentran en el DataFrame.")
            return  # No continuar si las columnas necesarias no existen

        # Crear una tabla pivote agrupando por 'classif2' y sumando los valores de 'obs_value'
        pivot_data = df.pivot_table(values='obs_value', index='classif2', aggfunc='sum')

        # Crear el gráfico de barras
        fig, ax = plt.subplots(figsize=(6, 4))
        pivot_data.plot(kind='bar', ax=ax)
        ax.set_title("Gráfico de Barras Agrupadas")
        ax.set_xlabel('Clasificación 2')
        ax.set_ylabel('Valor Observado')

        # Mostrar la figura en el frame
        self.mostrar_figura_en_frame(fig, frame)

    def mostrar_grafico_lineas(self, frame, df):
        """
        Muestra un gráfico de líneas en el frame indicado.

        Args:
            frame: Frame de Tkinter donde se dibujará el gráfico.
            df: DataFrame con los datos a graficar.
        """
        # Verificar que las columnas necesarias estén presentes
        if 'year' not in df.columns or 'classif2' not in df.columns or 'obs_value' not in df.columns:
            print("Error: Las columnas 'year', 'classif2' o 'obs_value' no se encuentran en el DataFrame.")
            return  # No continuar si las columnas necesarias no existen

        # Agrupar los datos por 'year' y 'classif2', luego graficar la suma de 'obs_value'
        fig, ax = plt.subplots(figsize=(6, 4))
        df.groupby(['year', 'classif2'])['obs_value'].sum().unstack().plot(ax=ax)
        ax.set_title("Progresión Temporal")
        ax.set_xlabel('Año')
        ax.set_ylabel('Valor Observado')

        # Mostrar la figura en el frame
        self.mostrar_figura_en_frame(fig, frame)

    def mostrar_figura_en_frame(self, figura, frame):
        """
        Dibuja la figura de Matplotlib dentro del frame de Tkinter.

        Args:
            figura: Figura de Matplotlib que contiene el gráfico.
            frame: Frame de Tkinter donde se dibujará la figura.
        """
        canvas = FigureCanvasTkAgg(figura, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
