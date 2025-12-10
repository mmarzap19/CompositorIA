# 🎵 CompositorIA – Generador de Canciones Educativas con IA

CompositorIA es una aplicación diseñada para crear **lecciones educativas** que luego serán utilizadas para generar **letras de canciones educativas** mediante Inteligencia Artificial.  


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

# ⚙️ Requerimientos previos
- Docker (necesario para n8n)
- IDE compatible con Python
- Postman



# 🚀 Instalación y ejecución de CompositorIA

Sigue estos pasos para ejecutar la aplicación desde cero:

## 1.  Clonar el repositorio
```bash
git clone https://github.com/mmarzap19/CompositorIA.git
cd budgetpartner-backend
```

## 2.  Instalar dependencias con requirements.txt

Este archivo contiene todas las dependencias necesarias para la instalación del proyecto.

```bash
pip install -r requirements.txt
```

## 3. Crear el archivo .env

En la raíz del proyecto, copia ".env.example" y añade las API KEYS indicadas:

```bash
OPENAI_KEY=tu_api_key_aqui
```

⚠️ Importante

    - Sin comillas
    - Sin espacios a los lados del =
    - No subir este archivo al repositorio

## 5.  Crear contenedor de n8n
1. Buscar y descargar "n8nio/n8n" en Docker
2. Lanzar el contenedor con el siguiente comando:
```bash
docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n --name n8n n8nio/n8n
```
3. Abrir en el navegador la dirección: http://localhost:5678⁠
4. Abrir los modelos almacenados en la carpeta n8n
5. Configurarlos en base a las instrucciones ubicadas en la carpeta


## 4.  Ejecutar la aplicación

```bash
python main.py
```