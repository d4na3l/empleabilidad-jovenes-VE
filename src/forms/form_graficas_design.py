import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.genering_graphs.oit_data_grapher import plot_pie_chart, plot_grouped_bar_chart, plot_line_chart


class FormularioGraficasDesign:
    def __init__(self, parent, df, title):
        """
        Inicializa el formulario y permite seleccionar gráficos a mostrar.

        Args:
            parent: Contenedor principal del formulario (Tkinter).
            df: DataFrame con los datos a graficar.
            title: Título del formulario y de los gráficos.
        """
        self.parent = parent
        self.cuerpo_principal = parent
        self.df = df
        self.title = title

        # Limpia el contenido del cuerpo principal antes de agregar nuevos elementos
        self.limpiar_cuerpo_principal()

        # Frame para el selector de gráficos
        self.selector_frame = tk.Frame(self.cuerpo_principal)
        self.selector_frame.pack(pady=10, fill='x')

        # Combobox para seleccionar gráficos
        self.grafico_selector = ttk.Combobox(
            self.selector_frame,
            values=["Gráfico de Pastel", "Gráfico de Barras Agrupadas", "Gráfico de Líneas"],
            state="readonly"
        )
        self.grafico_selector.set("Seleccionar gráfico")
        self.grafico_selector.pack(side=tk.LEFT, padx=10)

        # Botón para mostrar el gráfico seleccionado
        self.boton_mostrar = tk.Button(
            self.selector_frame,
            text="Mostrar Gráfico",
            command=self.mostrar_grafico_seleccionado
        )
        self.boton_mostrar.pack(side=tk.LEFT, padx=10)

        # Frame donde se mostrará el gráfico
        self.grafico_frame = tk.Frame(self.cuerpo_principal, width=600, height=400)
        self.grafico_frame.pack(pady=10, fill='both', expand=True)

    def limpiar_cuerpo_principal(self):
        """Limpia todos los widgets del cuerpo principal antes de mostrar nuevos gráficos."""
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_grafico_seleccionado(self):
        """
        Muestra el gráfico seleccionado en el combobox.
        """
        # Limpia el contenido del frame del gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Obtiene la selección actual del combobox
        grafico = self.grafico_selector.get()

        # Llama al método correspondiente según la selección
        try:
            if grafico == "Gráfico de Pastel":
                self.mostrar_grafico_pie(self.grafico_frame, self.df)
            elif grafico == "Gráfico de Barras Agrupadas":
                self.mostrar_grafico_barras(self.grafico_frame, self.df)
            elif grafico == "Gráfico de Líneas":
                self.mostrar_grafico_lineas(self.grafico_frame, self.df)
            else:
                raise ValueError("Selección inválida")
        except Exception as e:
            messagebox.showerror("Error al generar gráfico", str(e))

    def mostrar_grafico_pie(self, frame, df):
        """
        Muestra un gráfico de pastel en el frame indicado.
        """
        fig = plot_pie_chart(df, group_col='sex', value_col='obs_value', title=f'{self.title}, Sex Distribution')
        self.mostrar_figura_en_frame(fig, frame)

    def mostrar_grafico_barras(self, frame, df):
        """
        Muestra un gráfico de barras agrupadas en el frame indicado.
        """
        fig = plot_grouped_bar_chart(df, group_col='classif1', x_col='classif2', y_col='obs_value', title=self.title)
        self.mostrar_figura_en_frame(fig, frame)

    def mostrar_grafico_lineas(self, frame, df):
        """
        Muestra un gráfico de líneas en el frame indicado.
        """
        fig = plot_line_chart(df, time_col='time', classif2_col='classif2', y_col='obs_value', title=self.title)
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
