import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import pandas as pd
from src.processing_data.oit_data_processor import process_pipeline  # Importar la función process_pipeline
from util.util_rutas import obtener_ruta_absoluta


class FormularioSitioDataSets:
    def __init__(self, parent):
        self.parent = parent
        self.cuerpo_principal = parent
        self.df = None  # Agregamos una variable para almacenar el DataFrame
        self.title = None

        self.limpiar_cuerpo_principal()
        self.crear_barra_superior()
        self.mostrar_archivos_csv()

    def limpiar_cuerpo_principal(self):
        """Limpia todos los widgets del cuerpo principal."""
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def crear_barra_superior(self):
        """Configura la barra superior con un título."""
        barra_superior = tk.Frame(self.cuerpo_principal, bg="white")
        barra_superior.pack(side=tk.TOP, fill=tk.X)

        label_titulo = tk.Label(barra_superior, text="Conjunto de Datos", bg="white")
        label_titulo.config(fg="#222d33", font=("Roboto", 30))
        label_titulo.pack(pady=10)

    def mostrar_archivos_csv(self):
        """Muestra los archivos CSV disponibles en un combobox."""
        directorio_csv = obtener_ruta_absoluta("data/raw")

        try:
            archivos = [f for f in os.listdir(directorio_csv) if f.endswith('.csv')]
        except FileNotFoundError:
            archivos = []
            messagebox.showwarning("Advertencia", f"No se encontró el directorio: {directorio_csv}")

        frame_combobox = tk.Frame(self.cuerpo_principal, bg="white")
        frame_combobox.pack(pady=20, padx=10, fill='both', expand=True)

        self.combobox_archivos = ttk.Combobox(frame_combobox, values=archivos)
        self.combobox_archivos.pack(pady=5, fill='x')
        self.combobox_archivos.set("Selecciona un archivo CSV")

        boton_generar = tk.Button(frame_combobox, text="Generar DataFrames", command=self.generar_dataframes)
        boton_generar.pack(pady=5)

        boton_generar.config(bg="#4CAF50", fg="white", font=("Roboto", 12), relief=tk.RAISED, bd=2)
        boton_generar.bind("<Enter>", lambda e: e.widget.config(bg="#45a049"))
        boton_generar.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))

    def generar_dataframes(self):
        """Carga y muestra todos los DataFrames generados a partir del archivo CSV seleccionado."""
        archivo_seleccionado = self.combobox_archivos.get()
        self.title = ' '.join([part.upper() for part in archivo_seleccionado.split('.')[0].split('_')[1:-1]])

        if archivo_seleccionado:
            ruta_archivo = obtener_ruta_absoluta(f'data/raw/{archivo_seleccionado}')
            try:
                # Usar la función process_pipeline para procesar el archivo CSV
                rename_map = {
                    'sex.label': 'sex',
                    'classif1.label': 'classif1',
                    'classif2.label': 'classif2'
                }
                columns_to_keep = ['time', 'sex', 'classif1', 'classif2', 'obs_value']

                self.df = process_pipeline(ruta_archivo, rename_columns=rename_map, columns_to_keep=columns_to_keep)  # Guardamos el DataFrame

                # Mostrar el DataFrame en la ventana
                self.mostrar_dataframe(self.df, archivo_seleccionado)

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo procesar el archivo: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un archivo CSV.")

    def mostrar_dataframe(self, df, nombre_archivo):
        """Muestra el DataFrame en la ventana, usando un Treeview para hacerlo más legible."""
        # Limpiar el cuerpo principal antes de mostrar el nuevo DataFrame
        self.limpiar_cuerpo_principal()

        # Crear un Frame para el DataFrame
        frame_dataframe = tk.Frame(self.cuerpo_principal)
        frame_dataframe.pack(side=tk.TOP, padx=10, pady=(5, 20), fill='both', expand=True)

        # Mostrar el título del DataFrame con el nombre del archivo
        label_dataframe = tk.Label(frame_dataframe, text=f"DataFrame Cargado: {nombre_archivo}", bg="white")
        label_dataframe.pack(pady=5)

        # Crear un Treeview para mostrar el DataFrame
        tree = ttk.Treeview(frame_dataframe, columns=list(df.columns), show='headings')
        tree.pack(pady=5, fill='both', expand=True)

        # Definir las columnas y establecer un ancho fijo
        ancho_fijo = 150  # Ancho fijo para todas las columnas
        for col in df.columns:
            tree.heading(col, text=col)  # Títulos de las columnas
            tree.column(col, anchor="center", width=ancho_fijo)  # Alinear el contenido al centro y establecer ancho fijo

        # Insertar las primeras 6 y últimas 6 filas en el Treeview
        df_to_show = pd.concat([df.head(6), df.tail(6)])  # Concatenar las primeras y últimas 6 filas

        for index, row in df_to_show.iterrows():
            tree.insert("", "end", values=row.tolist())  # Insertar fila

        # Mostrar el total de filas y columnas
        total_filas, total_columnas = df.shape
        label_totales = tk.Label(frame_dataframe, text=f"Total de Filas: {total_filas}, Total de Columnas: {total_columnas}", bg="white")
        label_totales.pack(pady=5)

        # Crear un Frame para los botones en la esquina inferior
        frame_botones = tk.Frame(self.cuerpo_principal)
        frame_botones.pack(side=tk.BOTTOM, anchor='e', padx=10, pady=10)

        boton_ir_grafico = tk.Button(frame_botones, text="Ir al Gráfico", command=self.mostrar_panel_graficas)
        boton_ir_grafico.pack(side=tk.LEFT, padx=5)

        boton_borrar = tk.Button(frame_botones, text="Borrar Todo", command=self.borrar_todo)
        boton_borrar.pack(side=tk.LEFT, padx=5)

        boton_ir_grafico.config(bg="#4CAF50", fg="white", font=("Roboto", 12), relief=tk.RAISED, bd=2)
        boton_ir_grafico.bind("<Enter>", lambda e: e.widget.config(bg="#45a049"))
        boton_ir_grafico.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))

        boton_borrar.config(bg="#F44336", fg="white", font=("Roboto", 12), relief=tk.RAISED, bd=2)
        boton_borrar.bind("<Enter>", lambda e: e.widget.config(bg="#e53935"))
        boton_borrar.bind("<Leave>", lambda e: e.widget.config(bg="#F44336"))

    def mostrar_panel_graficas(self):
        """Cambia la vista al panel de gráficas."""
        if self.df is None:
            messagebox.showwarning("Advertencia", "Primero debes cargar un archivo CSV.")
            return

        self.limpiar_cuerpo_principal()  # Limpia el contenido actual del cuerpo principal
        # Crear la instancia de FormularioGraficasDesign y pasar el DataFrame
        from src.forms.form_graficas_design import FormularioGraficasDesign
        FormularioGraficasDesign(self.cuerpo_principal, self.df, self.title)  # Pasamos el df aquí

    def borrar_todo(self):
        """Borra el contenido actual y permite seleccionar un nuevo CSV."""
        self.limpiar_cuerpo_principal()
        self.crear_barra_superior()
        self.mostrar_archivos_csv()
