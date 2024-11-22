import tkinter as tk

class FormularioInfoDesign:
    """Formulario para mostrar información del sistema."""
    def __init__(self, parent):
        self.parent = parent  # Referencia al contenedor principal
        self.create_widgets()  # Inicializar widgets

    def create_widgets(self):
        """Crear y organizar los widgets específicos de esta vista."""
        # Limpiar contenido previo en el contenedor
        for widget in self.parent.winfo_children():
            widget.destroy()

        # Agregar un título
        label_titulo = tk.Label(self.parent, text="Información del Sistema",
                                font=("Roboto", 16, "bold"), bg="white")
        label_titulo.pack(pady=20)

        # Detalles del sistema
        label_version = tk.Label(self.parent, text="Versión: 1.0", font=("Roboto", 12), bg="white")
        label_version.pack(pady=10)

        label_author = tk.Label(self.parent, text="Autor: Alexander Azocar", font=("Roboto", 12), bg="white")
        label_author.pack(pady=10)
