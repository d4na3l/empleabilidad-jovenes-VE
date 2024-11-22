def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    # Obtiene el ancho de la pantalla en píxeles
    pantall_ancho = ventana.winfo_screenwidth()
    
    # Obtiene el alto de la pantalla en píxeles
    pantall_largo = ventana.winfo_screenheight()
    
    # Calcula la posición X para centrar la ventana en la pantalla
    x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))
    
    # Calcula la posición Y para centrar la ventana en la pantalla
    y = int((pantall_largo / 2) - (aplicacion_largo / 2))
    
    # Establece el tamaño de la ventana y su posición en la pantalla
    # La geometría se define como "ancho x alto + posición_x + posición_y"
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")