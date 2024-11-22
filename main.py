# Importa la clase FormularioMaestroDesign desde el módulo form_maestro_design
from formularios.form_maestro_design import FormularioMaestroDesign

# Crea una instancia de la clase FormularioMaestroDesign y la asigna a la variable 'app'.
# Al crear esta instancia, se ejecuta el método __init__, que configura la ventana y los componentes.
app = FormularioMaestroDesign()

# Inicia el bucle principal de la aplicación Tkinter.
app.mainloop()