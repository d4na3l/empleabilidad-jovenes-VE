# Importa el módulo tkinter y la constante COLOR_CUERPO_PRINCIPAL desde el archivo de configuración.
import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL

class FormularioSitioEquipo:
    
    def __init__(self, panel_principal):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal, bg="#ffffff")  # Cambiar color de fondo
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal, bg="#ffffff")  # Cambiar color de fondo
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto centrado
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Integrantes del Equipo")
        self.labelTitulo.config(fg="#000000", font=("Roboto", 30), bg="#ffffff")  # Cambiar color de fondo
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Llama a la función para mostrar los integrantes en la barra inferior
        self.mostrar_integrantes(self.barra_inferior)  # Cambiar a barra inferior
    
    def mostrar_integrantes(self, panel):
        # Lista de integrantes 
        integrantes = [
            {"nombre": "Cristhian  ", "rol": "Lider del Proyecto"},
            {"nombre": "Manuel Contreras ", "rol": "Secretaria"},
            {"nombre": "Sahid", "rol": "Limpieza de datos"},
            {"nombre": "janarotu Perez", "rol": "Limpieza de datos"},
            {"nombre": "Alexander Azocar", "rol": "Analista"},
        ]

        # Crear un Frame para contener los integrantes
        frame_integrantes = tk.Frame(panel, bg="#ffffff")  # Cambiar color de fondo
        frame_integrantes.pack(pady=20)

        # Agregar cada integrante a la interfaz y centrar el texto
        for integrante in integrantes:
            label = tk.Label(frame_integrantes, text=f"{integrante['nombre']} - {integrante['rol']}",
                             bg="#ffffff", fg="black", font=("Roboto", 12))  # Cambiar color de fondo
            label.pack(anchor="center", padx=10, pady=5)  # Cambiar anchor a "center"