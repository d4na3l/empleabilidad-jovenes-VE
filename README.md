# Análisis de Empleabilidad de Jóvenes en Venezuela

Nuestro proyecto se centra en la obtención, visualización y análisis de datos sobre el empleo juvenil en Venezuela, utilizando información proporcionada por la base de datos ILOSTAT de la Organización Internacional del Trabajo (OIT) y, en la medida de lo posible, complementada con datos locales del Instituto Nacional de Estadística (INE). Este análisis busca identificar patrones y tendencias clave en la empleabilidad de los jóvenes en el país.

## Tabla de contenidos

1. [Descripción](#descripción)
2. [Arquitectura del proyecto](#arquitectura-del-proyecto)
3. [Proceso de Desarrollo](#proceso-de-desarrollo)
4. [Funcionalidades extra](#funcionalidades-extra)
5. [Agradecimientos](#agradecimientos)

### Descripción

El proyecto estudia los criterios de empleabilidad de los jóvenes en Venezuela basándose en indicadores como subempleo, tipos de empleo, nivel de estudios, género, sector económico y otros parámetros. Los datos utilizados provienen principalmente de:

-   ILOSTAT (Organización Internacional del Trabajo)
-   INE Venezuela
    El proyecto está desarrollado en Python y utiliza bibliotecas como Pandas, Matplotlib y Tkinter para el procesamiento, análisis y visualización de datos.

### Arquitectura del proyecto

```
empleabilidad-jovenes-VE/
├── data/                 # Almacén de datasets
├── notebooks/            # Notebooks de Jupyter
├── src/                  # Código fuente
│   ├── forms/            # Interfaz gráfica
│   ├── genering_graphs/  # Generación de gráficos
│   └── processing_data/  # Procesamiento de datos
├── util/                 # Funciones globales
└── README.md
```

### Proceso de Desarrollo

1. Fuentes de datos

    - ILOSTAT (OIT) y datos locales del INE.
    - Periodo de análisis: 2005-2017 y 2020-2023.

2. Limpieza y procesamiento de datos

    - Se normalizan columnas y se categoriza la información por edad, género, sector económico, entre otros.
    - Identificación de valores atípicos y eliminación de inconsistencias.

3. Análisis estadístico

    - Uso de gráficos y estadísticas descriptivas para evaluar patrones de empleabilidad.

4. Documentación y pruebas

    - Validación de scripts en notebooks de Jupyter.

### Funcionalidades extra:

-   Desarrollo de Interfaz Gráfica de Usuario
    Tecnología/Herramientas utilizadas: Tkinter, Python.
    Arquitectura: Gestión de gráficos e interacción dinámica para explorar datos.

-   Visualización interactiva
    Creación de gráficos personalizados según los criterios seleccionados por el usuario

### Agradecimientos

Agradecemos a la Organización Internacional del Trabajo (OIT) y al Instituto Nacional de Estadística (INE) por proporcionar los datos que sustentan este proyecto.

## Instrucciones para Clonar el Repositorio y Convenciones de Colaboración

### Clonar el Repositorio

```bash
git clone https://github.com/d4na3l/empleabilidad-jovenes-VE
cd empleabilidad-jovenes-VE
```

### Convenciones de Colaboracion

Para colaborar en este proyecto, utilizaremos **conventional commits** como guía para mantener un historial de cambios claro y comprensible. Los siguientes tipos de commit están definidos para facilitar la organización y comprensión de las modificaciones:

-   **chore**: Modificaciones menores en la estructura o configuración.
    -   Ejemplo:
        -   `chore: añadir .gitignore para archivos temporales`
        -   `chore: actualizar dependencias en requirements.txt`
        -   `chore: reorganizar estructura de carpetas en /src`
-   **feat**: Agregar una nueva funcionalidad o script.
    -   Ejemplo:
        -   `feat: agregar script para análisis de empleabilidad`
        -   `feat: implementar función para procesar datos de la OIT`
        -   `feat: añadir visualización de tendencias de empleo`
-   **fix**: Corregir errores encontrados en el código o en la estructura.
    -   Ejemplo:
        -   `fix: corregir error en la carga de datos en analysis.py`
        -   `fix: solucionar problema de compatibilidad en data_processing.py`
        -   `fix: ajustar visualización en gráficos de empleabilidad`
-   **docs**: Cambios en la documentación.
    -   Ejemplo:
        -   `docs: actualizar README con instrucciones para configurar el entorno`
        -   `docs: añadir explicación de variables en analysis.py`
        -   `docs: corregir formato de ejemplo en documentación`
-   **refactor**: Cambios en el código que no alteran la funcionalidad pero mejoran la estructura.
    -   Ejemplo:
        -   `refactor: optimizar funciones de limpieza en data_processing.py`
        -   `refactor: simplificar lógica de análisis en analysis.py`
        -   `refactor: reorganizar funciones auxiliares en utils.py`

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

    - En Linux/macOS:

    ```bash
    python3 -m venv project
    ```

    - En Windows:

    ```cmd
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

## Instalar Dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

## Ejecutar el Proyecto

Después de instalar las dependencias, puedes ejecutar el proyecto con:

-   En Linux/macOS:

```bash
python3 main.py
```

-   En Windows:

```cmd
python main.py
```
