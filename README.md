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

## Instrucciones para Clonar el Repositorio y Convenciones de Colaboración

### Clonar el Repositorio
```bash
git clone https://github.com/d4na3l/empleabilidad-jovenes-VE
cd empleabilidad-jovenes-VE
```

### Convenciones de Colaboracion
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

## Flujo de trabajo con Git

1. Configuración de la Rama de Trabajo
    - Trabajaremos en la rama `develop` para probar y desarrollar nuevas funcionalidades. Para una organización adecuada, sigue estos pasos:

    #### Paso a Paso:

    - **Cambiar a la rama `develop`:**
   ```bash
   git checkout develop
   ```
    - **Actualizar la rama develop con los últimos cambios del repositorio:**
    ```bash
    git pull origin develop
    ```
    - **Crear una rama nueva para la funcionalidad específica (basada en develop):** Usa un nombre descriptivo para la nueva rama. Por ejemplo, si trabajas en el análisis de empleabilidad:
    ```bash
    git checkout -b feature/analisis-empleabilidad
    ```

2. Realizar Cambios y Subirlos al Repositorio
    - Después de completar el trabajo en tu rama, asegúrate de seguir estos pasos antes de abrir un pull request.

    #### Paso a Paso:
    - **Añadir los archivos que deseas confirmar al commit:**
    ```bash
    git add .
    ```
    - **Crear un commit con un mensaje descriptivo siguiendo el formato de conventional commits:**
    ```bash
    git commit -m "Commit que siga las convenciones previamente presentadas"
    ```
    - **Enviar la rama con tus cambios al repositorio:**
    ```bash
    git push origin feature/analisis-empleabilidad
    ```

3. Abrir un Pull Request para Revisión de Cambios
    - Una vez que los cambios estén en tu rama en GitHub, abre un pull request hacia la rama develop para revisión.

    #### Paso a Paso:
    - **Acceder al repositorio en GitHub.**
    - **Seleccionar la pestaña `Pull requests`.**
    - **Hacer clic en `New pull request`.**
    - **Seleccionar `develop` como rama de destino y tu rama `(feature/analisis-empleabilidad)` como rama de origen.**
    - **Escribir una descripción detallada del pull request explicando los cambios realizados.**
    - **Solicitar revisión para que el administrador pueda revisar y dar feedback.**

    **_NOTA:_** No fusionar el pull request a develop directamente. Solo el administrador tiene permisos para fusionar los cambios después de la revisión.

## Configurar el Ambiente Virtual

### Manual para Crear y Activar el Entorno Virtual

Si prefieres configurarlo manualmente, sigue estos pasos:

1. Crear el ambiente virtual:

    ```bash
    python3 -m venv project
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
## Instalar Dependencias
Una vez activado el entorno virtual, instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```
Después de seguir estas instrucciones, el entorno estará configurado y listo para su uso.
