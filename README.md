# Análisis de satisfacción con el SII — Encuesta ISC ITVER

Proyecto de la materia **Adquisición y Visualización de Datos**. Se analiza una encuesta simulada a estudiantes de Ingeniería en Sistemas Computacionales del ITVER sobre su satisfacción con el SII.

El notebook [`notebook.ipynb`](notebook.ipynb) contiene:

1. Carga del dataset desde Google Sheets (`encuesta_sii`).
2. Limpieza del dataset (renombrado de columnas, duplicados, tipos de dato, nulos).
3. **Intervalo 1:** proporción de satisfacción del bloque 1.º – 4.º semestre.
4. **Intervalo 2:** proporción de satisfacción del bloque 5.º – 9.º semestre.
5. **Diferencia de proporciones** entre ambos bloques.

## Requisitos

- [Python](https://www.python.org/downloads/) **3.11 o superior** (el proyecto se desarrolló con Python 3.14).
- [Git](https://git-scm.com/downloads).
- [Visual Studio Code](https://code.visualstudio.com/) con las extensiones **Python** y **Jupyter** de Microsoft.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/MarcoVargas0803/Pandas_proyecto_ciencia_datos.git
cd Pandas_proyecto_ciencia_datos
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

La carpeta `.venv` ya está en el `.gitignore`, por lo que no se sube a GitHub. Es importante asegurarse que cada archivo .`gitignore` se encuentre.

### 3. Activar el entorno virtual

| Sistema / terminal | Comando |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (CMD) | `.venv\Scripts\activate.bat` |
| Windows (Git Bash) | `source .venv/Scripts/activate` |
| macOS / Linux | `source .venv/bin/activate` |

Al activarlo verás `(.venv)` al inicio de la línea de la terminal.

> **Si PowerShell bloquea el script** con un error de "ejecución de scripts deshabilitada", ejecuta una vez:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

### 4. Instalar las dependencias

Con el entorno activado:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Esos comandos harán que instalen: **pandas 3.1.0**, **numpy 2.5.4** e **ipykernel** (necesario para ejecutar el notebook en VS Code).

Para comprobar que quedó instalado:

```bash
python -c "import pandas, numpy; print(pandas.__version__, numpy.__version__)"
```

## Ejecutar el notebook

1. Abre la carpeta del proyecto en VS Code.
2. Abre `notebook.ipynb`.
3. En la esquina superior derecha, haz clic en **Select Kernel** → **Python Environments** → elige el de **`.venv`**.
4. Ejecuta **Restart** y luego **Run All** para correr todas las celdas en orden.

> **Importante:** las celdas dependen de las anteriores (por ejemplo, la diferencia de proporciones usa los resultados de los intervalos 1 y 2). Ejecútalas siempre en orden; si ejecutas una celda suelta dos veces, algunos resultados pueden cambiar (por ejemplo, el conteo de duplicados).

## Agregar una nueva dependencia

Si instalas una librería nueva recuerda actualizar el `requirements.txt`:

```bash
pip install nombre_libreria
pip freeze > requirements.txt
```

Después haz commit del `requirements.txt` actualizado. De esta forma cuando se tenga que actualizar las dependencias de otro se utiliza: `pip install -r requirements.txt`.

## Integrantes

- Marco Antonio Vargas Valle
- Francisco Manuel Diaz Arenas
- Mario Mauricio Gudiño Barrios
