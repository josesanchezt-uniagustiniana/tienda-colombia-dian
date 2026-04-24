# Uniagustiniana - Simulador de Facturación Electrónica - Selección Colombia Store
## Docente José Sánchez

Este proyecto es una herramienta pedagógica diseñada para la **Universidad Agustiniana**. Su objetivo es demostrar el flujo técnico entre una interfaz de usuario moderna (E-commerce) y los requisitos legales de la **DIAN** en Colombia (Generación de XML UBL 2.1 y cálculo del CUFE).

---

## 🛠️ Stack Tecnológico
Basado en el modelo de aprendizaje, el proyecto utiliza:
* **Backend:** Python con **FastAPI** (Lógica de servidor).
* **Frontend:** HTML5 + **Tailwind CSS** (Interfaz moderna y responsiva).
* **Motor de Plantillas:** **Jinja2** (Renderizado dinámico).
* **Procesamiento XML:** **lxml** (Generación de estándar UBL 2.1).

---

## 📂 Estructura del Proyecto

Asegúrate de que tus carpetas se vean exactamente así:

```text
tienda-colombia-dian/
├── main.py                 # Lógica del servidor y generación de XML
├── static/                 # Archivos estáticos
│   ├── css/                # (Opcional si usas Tailwind CDN)
│   └── img/                # Fotos de las camisetas (local.jpg, visitante.jpg)
├── templates/              # Vistas HTML
│   ├── base.html           # Plantilla maestra (Layout)
│   └── index.html          # Página principal y consola técnica
├── facturas_generadas/     # Carpeta donde se guardarán los archivos .xml
└── uniagustiniana/         # Carpeta del Entorno Virtual (VENV)
```

# 🚀 Guía de Instalación y Ejecución

# 1. Preparar el Entorno Virtual
Abre una terminal en la carpeta de tu proyecto y ejecuta:

## Crear el entorno virtual
python -m venv uniagustiniana

## Activar el entorno en Windows
uniagustiniana\Scripts\activate

## Activar el entorno en Mac/Linux
source uniagustiniana/bin/activate

# 2. Instalar Librerías Necesarias
Con el entorno activado, instala las dependencias:
pip install -r requirements.txt

# 3. Ejecución del Servidor

Para iniciar el simulador, ejecuta el siguiente comando:

```Bash
python main.py
```

El servidor estará disponible en: http://127.0.0.1:8000

![Pagina de Inicio](/static/img/inicio.png)