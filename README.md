# 🎵 CompositorIA – Generador de Canciones Educativas con IA

CompositorIA es una aplicación diseñada para crear **lecciones educativas** que luego serán utilizadas para generar **letras de canciones educativas** mediante Inteligencia Artificial.  
El proyecto usa Python, Flask, la API de OpenAI y variables de entorno `.env`.


## 🚀 Características principales

- Generación automática de **lecciones educativas completas**.
- Contenido optimizado para convertirse en letras musicales.
- Backend modular escrito en Python.
- Uso de `.env` para claves privadas.
- Integración con modelos GPT (OpenAI).


## 📁 Estructura del proyecto


    CompositorIA/
    │
    ├── service/
    │ └── lesson_service.py
    │
    ├── app.py
    ├── .env
    ├── requirements.txt
    └── README.md




# ⚙️ Instalación y ejecución de CompositorIA

Sigue estos pasos para ejecutar la aplicación desde cero:

## 1.  Clonar el repositorio

```bash
## VSC y au (ya se cambiará)
```
## 2.  Instalar dependencias con requirements.txt

Este archivo contiene todas las dependencias necesarias.

```bash
pip install -r requirements.txt
```

## 3. Crear el archivo .env

En la raíz del proyecto, crea:

```bash
OPENAI_KEY=tu_api_key_aqui
```

⚠️ Importante

 - Sin comillas
 - Sin espacios a los lados del =
 - No subir este archivo al repositorio

## 4.  Ejecutar la aplicación

```bash
python main.py
```