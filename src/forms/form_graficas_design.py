import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormularioGraficasDesign:
    def __init__(self, parent):
        self.parent = parent  # Recibimos el contenedor principal
        self.cuerpo_principal = parent

        self.dataframes = self.crear_dataframes()  # Inicializa los DataFrames

        # Limpia el contenido del cuerpo principal antes de agregar nuevos elementos
        self.limpiar_cuerpo_principal()

        # Elementos de UI
        self.selector_dataframes = self.crear_selector()
        self.selector_dataframes.pack(pady=10)

        # Configurar figura y canvas
        self.figura, self.canvas = self.crear_canvas()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Mostrar el gráfico inicial
        self.selector_dataframes.current(0)
        self.mostrar_grafico()

    def limpiar_cuerpo_principal(self):
        """Limpia todos los widgets del cuerpo principal."""
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def crear_dataframes(self):
        """Crear y devolver los DataFrames para los gráficos."""
        return {
            'DataFrame 1': pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]}),
            'DataFrame 2': pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [1, 3, 2, 5, 4]}),
            'DataFrame 3': pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [5, 3, 4, 2, 1]}),
        }

    def crear_selector(self):
        """Crear y configurar el selector de DataFrames."""
        selector = ttk.Combobox(self.cuerpo_principal, values=list(self.dataframes.keys()))
        selector.bind("<<ComboboxSelected>>", self.mostrar_grafico)
        return selector

    def crear_canvas(self):
        """Crear y devolver la figura y el canvas del gráfico."""
        figura = Figure(figsize=(8, 6), dpi=100)
        canvas = FigureCanvasTkAgg(figura, master=self.cuerpo_principal)
        return figura, canvas

    def mostrar_grafico(self, event=None):
        """Actualizar el gráfico basado en el DataFrame seleccionado."""
        self.figura.clear()  # Limpiar la figura

        # Obtener el DataFrame seleccionado
        nombre_df = self.selector_dataframes.get()
        if not nombre_df:  # Validación en caso de que el selector esté vacío
            return

        df = self.dataframes[nombre_df]

        # Crear un nuevo gráfico
        ax = self.figura.add_subplot(111)
        ax.plot(df['X'], df['Y'], marker='o', label=nombre_df)
        ax.set_title(f'Gráfico de {nombre_df}')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        # Redibujar el canvas
        self.canvas.draw()
