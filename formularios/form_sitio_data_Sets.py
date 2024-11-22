import tkinter as tk
from tkinter import font, messagebox
import os
import pandas as pd
import subprocess  # Para abrir archivos con la aplicación predeterminada

class Formulario_sitio_data_Sets():
    def __init__(self, panel_principal):
        # Establecer el color de fondo de la ventana principal
        panel_principal.config(bg="white")

        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal, bg="white")
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal, bg="white")
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Conjunto de datos", bg="white")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg="white")
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Mostrar archivos CSV
        self.mostrar_archivos_csv(self.barra_inferior)

    def mostrar_archivos_csv(self, panel):
        # Directorio donde se encuentran los archivos CSV
        directorio_csv = "./csv_files"  # Cambia esto a tu directorio de archivos CSV

        # Obtener la lista de archivos CSV
        archivos = [f for f in os.listdir(directorio_csv) if f.endswith('.csv')]

        # Crear un marco para los botones
        frame_botones = tk.Frame(panel, bg="white")
        frame_botones.pack(pady=20, padx=10, fill='both', expand=True)

        # Crear un botón para cada archivo CSV
        for archivo in archivos:
            boton = tk.Button(frame_botones, text=archivo, command=lambda f=archivo: self.abrir_archivo_csv(f))
            boton.pack(pady=5, fill='x')
            # Estilo del botón
            boton.config(bg="#4CAF50", fg="white", font=("Roboto", 12), relief=tk.RAISED, bd=2)
            boton.bind("<Enter>", lambda e: e.widget.config(bg="#45a049"))  # Cambiar color al pasar el mouse
            boton.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))  # Volver al color original

    def abrir_archivo_csv(self, archivo):
        # Ruta completa del archivo
        ruta_archivo = os.path.join("./csv_files", archivo)  # Cambia esto a tu directorio de archivos CSV

        try:
            # Abrir el archivo CSV con la aplicación predeterminada (Excel)
            subprocess.Popen(['start', 'excel', ruta_archivo], shell=True)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")



