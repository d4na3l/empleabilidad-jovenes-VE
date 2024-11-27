import util.util_rutas as util_rutas  # Asumiendo que el archivo de utilidades está en util/

from PIL import Image, ImageTk

def leer_imagen(ruta_relativa, tamaño):
    """
    Lee y devuelve una imagen redimensionada.

    Args:
        ruta_relativa (str): Ruta relativa al archivo de la imagen.
        tamaño (tuple): Dimensiones a las que se redimensionará la imagen.

    Returns:
        ImageTk.PhotoImage: Objeto de imagen redimensionada o None si ocurre un error.
    """
    try:
        # Convertir la ruta relativa en ruta absoluta
        ruta_absoluta = util_rutas.obtener_ruta_absoluta(ruta_relativa)
        imagen = Image.open(ruta_absoluta)
        imagen = imagen.resize(tamaño)
        return ImageTk.PhotoImage(imagen)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None
