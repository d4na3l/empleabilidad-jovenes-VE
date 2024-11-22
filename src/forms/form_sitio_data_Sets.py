import tkinter as tk
from tkinter import messagebox
import os
import subprocess

class FormularioSitioDataSets:
    def __init__(self, parent):
        self.parent = parent  # Contenedor principal
        self.cuerpo_principal = parent

        # Limpia el contenido del cuerpo principal antes de agregar nuevos elementos
        self.limpiar_cuerpo_principal()

        self.crear_barra_superior()  # Configurar barra superior
        self.mostrar_archivos_csv()  # Mostrar los archivos CSV disponibles

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
        """Muestra los archivos CSV disponibles en un panel."""
        directorio_csv = "./data/raw"  # Cambia esto a tu directorio de archivos CSV

        # Obtener la lista de archivos CSV
        try:
            archivos = [f for f in os.listdir(directorio_csv) if f.endswith('.csv')]
        except FileNotFoundError:
            archivos = []
            messagebox.showwarning("Advertencia", f"No se encontró el directorio: {directorio_csv}")

        # Crear un marco para los botones
        frame_botones = tk.Frame(self.cuerpo_principal, bg="white")
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
        """Abre un archivo CSV con la aplicación predeterminada."""
        ruta_archivo = os.path.join("./data/raw", archivo)

        try:
            # Abrir el archivo CSV con la aplicación predeterminada
            subprocess.Popen(['start', 'excel', ruta_archivo], shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
