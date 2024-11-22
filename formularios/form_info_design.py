# Importa el módulo tkinter y un módulo utilitario para manejar ventanas.
import tkinter as tk
import util.util_ventana as util_ventana  # Asegúrate de que este módulo esté disponible

class FormularioInfoDesign(tk.Toplevel):
    def __init__(self, parent=None) -> None:
        # Llama al constructor de Toplevel con el padre
        super().__init__(parent)
        self.config_window()  # Configura la ventana
        self.contruirWidget()  # Construye los widgets de la ventana

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Empleabilidad')  # Establece el título de la ventana
        self.iconbitmap("./imagenes/logo.ico")  # Establece el icono de la ventana
        w, h = 400, 100  # Define el ancho y alto de la ventana
        util_ventana.centrar_ventana(self, w, h)  # Centra la ventana en la pantalla

    def contruirWidget(self):
        # Crea y configura los widgets de la ventana
        self.labelVersion = tk.Label(self, text="Version : 1.0")  # Crea un Label para la versión
        self.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)  # Configura el Label
        self.labelVersion.pack()  # Agrega el Label a la ventana

        self.labelAutor = tk.Label(self, text="Autor : Alexander Azocar")  # Crea un Label para el autor
        self.labelAutor.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)  # Configura el Label
        self.labelAutor.pack()  # Agrega el Label a la ventana