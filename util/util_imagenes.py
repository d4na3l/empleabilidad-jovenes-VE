from PIL import Image, ImageTk

def leer_imagen(ruta, tamaño):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño)
        return ImageTk.PhotoImage(imagen)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None
