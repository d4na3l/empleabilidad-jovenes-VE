import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficasDesign:

    def __init__(self, panel_principal):
        self.panel_principal = panel_principal
        
        # Crear algunos DataFrames de ejemplo
        self.dataframes = {
            'DataFrame 1': pd.DataFrame({
                'X': [1, 2, 3, 4, 5],
                'Y': [2, 4, 6, 8, 10]
            }),
            'DataFrame 2': pd.DataFrame({
                'X': [1, 2, 3, 4, 5],
                'Y': [1, 3, 2, 5, 4]
            }),
            'DataFrame 3': pd.DataFrame({
                'X': [1, 2, 3, 4, 5],
                'Y': [5, 3, 4, 2, 1]
            })
        }

        # Crear un combobox para seleccionar el DataFrame
        self.selector_dataframes = ttk.Combobox(panel_principal, values=list(self.dataframes.keys()))
        self.selector_dataframes.bind("<<ComboboxSelected>>", self.mostrar_grafico)
        self.selector_dataframes.pack(pady=10)

        # Crear la figura y el canvas
        self.figura = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figura, master=panel_principal)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Mostrar el gráfico por defecto
        self.selector_dataframes.current(0)  # Seleccionar el primer DataFrame por defecto
        self.mostrar_grafico()

    def mostrar_grafico(self, event=None):
        # Limpiar la figura actual
        self.figura.clear()

        # Obtener el DataFrame seleccionado
        nombre_df = self.selector_dataframes.get()
        df = self.dataframes[nombre_df]

        # Crear un nuevo eje
        ax = self.figura.add_subplot(111)

        # Graficar los datos del DataFrame
        ax.plot(df['X'], df['Y'], marker='o', label=nombre_df)
        ax.set_title(f'Gráfico de {nombre_df}')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        # Redibujar el canvas
        self.canvas.draw()
