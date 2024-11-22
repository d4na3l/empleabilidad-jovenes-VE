import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.form_graficas_design import FormularioGraficasDesign
from formularios.form_sitio_data_Sets import Formulario_sitio_data_Sets
from formularios.form_info_design import FormularioInfoDesign
from formularios.from_sitio_equipo import FormularioSitioEquipo

class FormularioMaestroDesign(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (700, 500))
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))
        self.imagenes = [self.logo, self.perfil]
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
        
        self.pantallas = []  # Pila para almacenar las pantallas visitadas
        self.mostrar_formulario_maestro()  # Mostrar el formulario maestro al inicio

    def config_window(self):
        self.title('Empleabilidad-jovenes-VE')
        self.iconbitmap("./imagenes/logo.ico")
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
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.buttonDashBoard = tk.Button(self.menu_lateral)        
        self.buttonProfile = tk.Button(self.menu_lateral)        
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)        
        self.buttonInicio = tk.Button(self.menu_lateral) 

        buttons_info = [
            ("Dashboard", "\uf109", self.buttonDashBoard, self.abrir_panel_graficas),
            ("DataSets", "\uf007", self.buttonProfile, self.abrir_sitio_data_sets),
            ("Equipo", "\uf03e", self.buttonPicture, self.abrir_panel_equipo),
            ("Info", "\uf129", self.buttonInfo, self.abrir_panel_info),  # Asegúrate de que este método esté bien definido
            ("Inicio", "\uf013", self.buttonInicio, self.mostrar_formulario_maestro)  # Asignar función al botón
        ]

        for text, icon, button, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)                    
    
    def controles_cuerpo(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)        
  
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command=comando)
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

    def abrir_panel_graficas(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        panel = FormularioGraficasDesign(self.cuerpo_principal)  # Crear el panel
        panel.pack(fill='both', expand=True)  # Empaquetar el panel
        self.pantallas.append(panel)  # Agregar a la pila
        
    def abrir_sitio_data_sets(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        panel = Formulario_sitio_data_Sets(self.cuerpo_principal)  # Crear el panel
        panel.pack(fill='both', expand=True)  # Empaquetar el panel
        self.pantallas.append(panel)  # Agregar a la pila

    def abrir_panel_info(self):           
        self.limpiar_panel(self.cuerpo_principal)     
        panel = FormularioInfoDesign(self)  # Pasar la ventana principal como padre
        panel.pack(fill='both', expand=True)  # Empaquetar el panel
        self.pantallas.append(panel)  # Agregar a la pila
    
    def abrir_panel_equipo(self):
        self.limpiar_panel(self.cuerpo_principal)     
        panel = FormularioSitioEquipo(self.cuerpo_principal)  # Crear el panel
        panel.pack(fill='both', expand=True)  # Empaquetar el panel
        self.pantallas.append(panel)  # Agregar a la pila    
    
    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def mostrar_formulario_maestro(self):
        self.limpiar_panel(self.cuerpo_principal)  # Limpiar el panel
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)  # Mostrar la imagen
        label.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar la imagen en el panel
        self.pantallas.clear()  # Limpiar la pila de pantallas

