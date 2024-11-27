import os
from pathlib import Path

def obtener_ruta_absoluta(ruta_relativa):
    """
    Devuelve la ruta absoluta para un archivo o directorio dado su ruta relativa.

    Args:
        ruta_relativa (str): Ruta relativa al directorio raíz del proyecto.

    Returns:
        str: Ruta absoluta compatible con el sistema operativo.
    """
    # Obtener el directorio raíz del proyecto (donde está el main)
    directorio_raiz = Path(__file__).resolve().parent.parent  # Ajustar según la estructura del proyecto
    ruta_absoluta = directorio_raiz / ruta_relativa
    return str(ruta_absoluta)


