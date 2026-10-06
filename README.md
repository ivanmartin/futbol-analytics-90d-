# ('futbol-analytics-90d-')
Repositorio inicial para subir mis primeros 90 días de proyectos aprendiendo análisis de datos enfocado en fútbol.
Objetivos: Estructurar, procesar y visualizar datos de eventos de partidos utilizando Python.

## Instalación y Configuración

Este documento recopila de forma cronológica y ordenada todos los comandos, atajos de teclado y soluciones técnicas que funcionan para levantar el entorno de trabajo desde cero en cualquier ordenador.

---

## FASE 1: Configuración de Miniconda y Entorno Virtual

Todo el proceso comienza en la terminal nativa de **Miniconda Prompt** (o Anaconda Prompt). Ejecuta los siguientes comandos en este orden estricto:

### 1. Verificación Base
Comprueba que las herramientas están instaladas correctamente en el sistema:
```bash
conda --version
python --version
```

### 2. Creación y Activación del Entorno. El proyecto actual se creó con 3.12.14
Creamos el entorno aislado con la versión de Python más reciente y lo activamos:
```bash
conda create -n futbol_env python=3.14 -y
conda activate futbol_env
```

### 3. Instalación de Dependencias
Instalamos todas las librerías necesarias para el análisis deportivo y los cuadernos interactivos:
```bash
pip install pandas statsbombpy mplsoccer matplotlib pyarrow ipykernel
```

### 4. Prueba de Humo Inmediata
Verificamos directamente en la terminal que todas las librerías se importan sin errores:
```bash
python -c "import pandas, statsbombpy, mplsoccer, matplotlib; print('OK')"
```
* **Si devuelve `OK`:** Todo está perfecto. Avanza al punto 6.
* **Si falla y llevas 20 minutos atascado:** Puede deberse a una incompatibilidad temporal de la versión de Python. Crea un entorno alternativo con una versión ultraestable ejecutando:
  ```bash
  conda create -n futbol_env312 python=3.12 -y 
  conda activate futbol_env312
  # Repite el paso 3 (pip install...) y vuelve a probar.
  ```

### 5. Congelar Requerimientos
Una vez que la prueba de humo de `OK`, guarda la foto exacta de tus librerías para poder replicarla al instante en el futuro:
```bash
pip freeze > requirements.txt
```

---

## FASE 2: Configuración e Inyección en Visual Studio Code

Una vez que el motor de Python está listo en la terminal, pasamos a configurar el editor de código.

### 1. Instalación de Extensiones Críticas
Abre VS Code e instala las dos extensiones oficiales de Microsoft desde el menú lateral (`Ctrl + Shift + X`):
* **Python**
* **Jupyter**

### 2. Selección Manual del Intérprete
1. Abre la barra de comandos del programa usando el atajo de teclado:
   * **`Ctrl + Shift + P`** (en Windows/Linux)
   * **`Cmd + Shift + P`** (en Mac)
2. Escribe en el buscador: **`Python: Select Interpreter`** y pulsa Intro.
3. Selecciona la opción: **`+ Enter interpreter path...`** (Introducir ruta del intérprete).
4. Pega la ruta física de tu entorno de Miniconda (ej. `C:\Users\Mec\miniconda3\envs\futbol_env\python.exe`) y pulsa Intro.

### 3. Qué hacer si VS Code no encuentra el entorno (El Truco de la Inyección)
Si el editor se queda congelado, lanza el error `An Invalid Python interpreter is selected` o las terminales integradas no reconocen tus comandos, aplica la solución definitiva:
1. **Cierra VS Code por completo.**
2. Vuelve a tu terminal nativa de **Miniconda Prompt** (donde tu indicador muestra correctamente `(futbol_env)`).
3. Viaja hasta la carpeta de tu proyecto usando el comando `cd`.
4. Abre VS Code desde esa misma línea de comandos escribiendo exactamente:
   ```bash
   code .
   ```
   *Al abrirse mediante este comando, VS Code se ve obligado a heredar todas las rutas y variables del sistema de la terminal activa.*

### 4. Verificación de la Terminal Integrada y Test de Campo
1. Con el editor abierto mediante el método anterior, ve al menú superior y haz clic en **Terminal** -> **New Terminal**.
2. Comprueba que abajo se abre la consola mostrando el indicador del entorno: `(futbol_env) C:\Users\Mec>`.
3. Crea un archivo llamado `test.py` y pega el código base de `mplsoccer`.
4. Haz **clic derecho en cualquier parte del código** y selecciona la opción: **`Run Python File in Terminal`** para generar tu primer campo de fútbol flotante en pantalla.

*Nota de optimización:* Si al abrir la carpeta se inicia un proceso infinito abajo que dice *"Loading projects"*, ve al menú de Extensiones (`Ctrl + Shift + X`), busca la extensión llamada **C#** (de Microsoft) y haz clic en **Disable** (Desactivar) para aligerar el editor.

---

## FASE 3: Configuración del Cuaderno de Jupyter (.ipynb)

Para trabajar de manera interactiva viendo tus tablas y gráficos integrados en la misma pantalla, sigue estos pasos:

1. Crea un archivo nuevo en tu carpeta de proyecto llamado **`analisis.ipynb`** (la extensión `.ipynb` es obligatoria).
2. Abre el archivo. En la esquina superior derecha del cuaderno, haz clic en el botón **`Select Kernel`** (Seleccionar núcleo) -> **Python Environments...** y marca tu entorno **`futbol_env`**.
3. Escribe tu código en la primera celda en blanco y ejecútala pulsando el botón **Play ▶** o usando el atajo **`Shift + Intro`**.
4. La primera vez que lo hagas, VS Code mostrará un aviso flotante preguntando si deseas instalar el paquete `ipykernel` para permitir la comunicación. Haz clic en **Sí / Instalar**.
5. Tras unos segundos de descarga, todos tus mapas de pases, mapas de calor y analíticas se renderizarán **directamente debajo de las celdas de código**.

## Origen de los Datos

* **Data:** [StatsBomb Open Data](https://github.com/statsbomb/open-data)
