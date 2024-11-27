import tkinter as tk

class FormularioSitioEquipo:
    """Formulario para mostrar información sobre los integrantes del equipo."""

    def __init__(self, parent):
        self.parent = parent  # Guardamos referencia al contenedor principal

        # Configurar widgets para esta vista
        self.crear_widgets()

    def crear_widgets(self):
        """Crear y organizar los widgets de la vista."""
        # Limpiar contenido previo en el contenedor
        for widget in self.parent.winfo_children():
            widget.destroy()

        # Barra superior con título
        barra_superior = tk.Frame(self.parent, bg="white", height=50)
        barra_superior.pack(fill=tk.X, padx=10, pady=10)

        label_titulo = tk.Label(
            barra_superior,
            text="Equipo del Proyecto",
            font=("Roboto", 16, "bold"),
            bg="white",
            fg="#222d33",
            anchor="center",
        )
        label_titulo.pack(fill=tk.BOTH, expand=True)

        # Mostrar la lista de integrantes en el panel principal
        self.mostrar_integrantes()

    def mostrar_integrantes(self):
        """Muestra la lista de integrantes del equipo."""
        # Lista de integrantes
        integrantes = [
            {"nombre": "Christian Rincón", "rol": "Líder del Proyecto"},
            {"nombre": "Manuel Contreras", "rol": "Encargado de documentación"},
            {"nombre": "Alexander Azócar", "rol": "Diseñador"},
            {"nombre": "Sahid Acosta", "rol": "Procesamiento de datos"},
            {"nombre": "Janarotu Pérez", "rol": "Búsqueda y filtro de datos"},
        ]

        # Contenedor para la lista de integrantes
        contenedor_lista = tk.Frame(self.parent, bg="white")
        contenedor_lista.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Crear etiquetas para cada integrante
        for integrante in integrantes:
            integrante_label = tk.Label(
                contenedor_lista,
                text=f"{integrante['nombre']} - {integrante['rol']}",
                font=("Roboto", 12),
                bg="white",
                anchor="w",
            )
            integrante_label.pack(fill=tk.X, pady=5, padx=10)
