# Análisis de Empleabilidad en Jóvenes en Venezuela

## Objetivo del Proyecto

Este proyecto busca analizar la empleabilidad de los jóvenes en Venezuela utilizando datos de la Organización Internacional del Trabajo (OIT) y otros recursos relevantes. Los objetivos específicos incluyen:

1. **Estudio de causas del desempleo**: Visualizar los factores más comunes del desempleo juvenil en Venezuela.

El proyecto está construido en Python, y se emplearán análisis de datos y visualizaciones para presentar las tendencias de empleabilidad en este grupo en particular.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
analisis_empleabilidad_jovenes/
├── data/                           # Almacena los datasets y archivos de datos
│   ├── raw/                        # Datos sin procesar
│   └── processed/                  # Datos limpios y procesados
├── notebooks/                      # Notebooks de Jupyter para análisis exploratorio y visualización
├── src/                            # Código fuente principal del proyecto
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación básica del proyecto
└── .gitignore                      # Archivos y carpetas ignoradas por Git
```

## Metodología de Trabajo

Desarrollaremos este proyecto haciendo entrega de cada unas de las asginaciones semanales que se nos pidan, para agilizar trabajo utilizaremos **notebooks de Jupyter**, de esa forma contribuiremos al análisis exploratorio y visualización de datos. El enfoque modular del código facilitará la ampliación y modificación de cada aspecto del proyecto a medida que avancemos. Todo el código principal será almacenado en la carpeta `src/`, lo que permitirá una gestión clara y eficiente de los scripts relacionados con el procesamiento de datos, análisis y modelos.

## Instrucciones de Uso de Git y Convenciones de Colaboración

Para colaborar en este proyecto, utilizaremos **conventional commits** como guía para mantener un historial de cambios claro y comprensible. Los siguientes tipos de commit están definidos para facilitar la organización y comprensión de las modificaciones:

- **chore**: Modificaciones menores en la estructura o configuración.
    - Ejemplo:
        - `chore: añadir .gitignore para archivos temporales`
        - `chore: actualizar dependencias en requirements.txt`
        - `chore: reorganizar estructura de carpetas en /src`
- **feat**: Agregar una nueva funcionalidad o script.
    - Ejemplo:
        - `feat: agregar script para análisis de empleabilidad`
        - `feat: implementar función para procesar datos de la OIT`
        - `feat: añadir visualización de tendencias de empleo`
- **fix**: Corregir errores encontrados en el código o en la estructura.
    - Ejemplo:
        - `fix: corregir error en la carga de datos en analysis.py`
        - `fix: solucionar problema de compatibilidad en data_processing.py`
        - `fix: ajustar visualización en gráficos de empleabilidad`
- **docs**: Cambios en la documentación.
    - Ejemplo:
        - `docs: actualizar README con instrucciones para configurar el entorno`
        - `docs: añadir explicación de variables en analysis.py`
        - `docs: corregir formato de ejemplo en documentación`
- **refactor**: Cambios en el código que no alteran la funcionalidad pero mejoran la estructura.
    - Ejemplo:
        - `refactor: optimizar funciones de limpieza en data_processing.py`
        - `refactor: simplificar lógica de análisis en analysis.py`
        - `refactor: reorganizar funciones auxiliares en utils.py`

### Flujo de trabajo con Git

1. Rama de trabajo:
     - Trabaja sobre la rama develop para desarrollar y probar nuevas funcionalidades.
     - Si trabajas en una funcionalidad específica, crea una rama con un nombre descriptivo basado en develop (por ejemplo, feature/analisis-empleabilidad).

3. Revisión de cambios:
     - Una vez hayas completado la tarea, sube los cambios a tu rama y abre un pull request hacia develop.
     - Se revisará el pull request, proporcionando feedback si es necesario.

4. Fusión a main:
     - Solo el lider podrá aprobar y realizar el merge a main después de revisar el pull request en develop.
     - Una vez que los cambios estén aprobados y probados en develop, el administrador será quien los fusione en main.

## Instrucciones para Clonar el Repositorio y Configurar el Entorno

### Clonar el Repositorio
```bash
git clone https://github.com/d4na3l/empleabilidad-jovenes-VE
cd empleabilidad-jovenes-VE
```

### Configurar el Ambiente Virtual

#### Manual para Crear y Activar el Entorno Virtual

Si prefieres configurarlo manualmente, sigue estos pasos:

1. Crear el ambiente virtual:

    ```bash
    python -m venv project
    ```

2. Activar el ambiente virtual:

    - En Linux/macOS:

        ```bash
        source project/bin/activate
        ```

    - En Windows:

        ```cmd
        project\Scripts\activate
        ```
### Instalar Dependencias Una vez activado el entorno virtual, instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```
Después de seguir estas instrucciones, el entorno estará configurado y listo para su uso.
