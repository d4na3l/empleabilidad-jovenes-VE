# Importa las clases ImageTk y Image del módulo PIL (Python Imaging Library).
# ImageTk se utiliza para trabajar con imágenes en aplicaciones Tkinter,
from PIL import ImageTk, Image

def leer_imagen(path, size):
    # Abre la imagen desde la ruta especificada utilizando Image.open().
    # La ruta 'path' debe ser una cadena que indique la ubicación del archivo de imagen.
    # 'size' es una tupla que especifica el nuevo tamaño de la imagen.
    # La imagen se redimensiona utilizando el método resize() de la clase Image.
    
    # El método resize() toma dos argumentos: el nuevo tamaño y el método de adaptación.
    # Image.ADAPTIVE se utiliza para ajustar la imagen a las dimensiones especificadas
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))