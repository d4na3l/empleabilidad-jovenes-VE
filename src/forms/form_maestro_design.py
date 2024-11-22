import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./img/logo.png", (700, 500))
        self.perfil = util_img.leer_imagen("./img/Perfil.png", (100, 100))
        self.imagenes = [self.logo, self.perfil]
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Empleabilidad Jovenes VE')
        # self.iconbitmap("./img/logo.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Generación Mccarthy")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=15, width=20)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior, text="https://github.com/d4na3l/empleabilidad-jovenes-VE")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=30, width=40)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        font_awesome = font.Font(family='FontAwesome', size=15)
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        buttons_info = [
            ("Dashboard", "\uf109", self.mostrar_panel_graficas),
            ("DataSets", "\uf007", self.mostrar_sitio_data_sets),
            ("Equipo", "\uf03e", self.mostrar_panel_equipo),
            ("Info", "\uf129", self.mostrar_panel_info),
            ("Inicio", "\uf013", self.mostrar_formulario_maestro)
        ]
        for text, icon, comando in buttons_info:
            self.configurar_boton_menu(text, icon, font_awesome, comando)

    def controles_cuerpo(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, text, icon, font_awesome, comando):
        button = tk.Button(self.menu_lateral, text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                           bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=20, height=2, command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_panel(self):
        """Limpia el panel de la vista principal."""
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    # Métodos para abrir diferentes vistas
    def mostrar_panel_graficas(self):
        """Cambia la vista al panel de gráficas."""
        self.limpiar_panel()  # Limpia el contenido actual del cuerpo principal
        from src.forms.form_graficas_design import FormularioGraficasDesign
        FormularioGraficasDesign(self.cuerpo_principal)  # Crea y muestra el nuevo panel


    def mostrar_sitio_data_sets(self):
        """Cambia la vista al panel de conjunto de datos."""
        self.limpiar_panel()  # Limpia el contenido actual del cuerpo principal
        from src.forms.form_sitio_data_Sets import FormularioSitioDataSets
        FormularioSitioDataSets(self.cuerpo_principal)  # Crea y muestra el nuevo panel


    def mostrar_panel_info(self):
        """Cambia la vista al panel de información del sistema."""
        self.limpiar_panel()  # Limpia el contenido actual del cuerpo principal
        from src.forms.form_info_design import FormularioInfoDesign
        FormularioInfoDesign(self.cuerpo_principal)  # Inicializa y muestra el nuevo panel


    def mostrar_panel_equipo(self):
        """Cambia la vista al panel de información del equipo."""
        self.limpiar_panel()  # Limpia el contenido actual del cuerpo principal
        from src.forms.form_sitio_equipo import FormularioSitioEquipo
        FormularioSitioEquipo(self.cuerpo_principal)  # Inicializa y muestra el nuevo panel


    def mostrar_formulario_maestro(self):
        self.limpiar_panel()
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
