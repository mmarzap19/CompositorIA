# service/lesson_service.py
from openai import OpenAI
from google import genai 
from dotenv import load_dotenv
import os

load_dotenv()  # carga las vars del archivo .env

BASE_PROMPT = """
Eres un asistente especializado en crear contenido educativo diseñado para convertirse después en la letra de una canción.

Tu tarea es generar una LECCIÓN EDUCATIVA COMPLETA, clara y atractiva, que luego será transformada en una canción con letra educativa.

La lección debe cumplir estos requisitos:

1. **Título de la lección**
2. **Objetivo educativo** (qué se desea enseñar)
3. **Explicación del concepto**, sencilla, precisa y adecuada para público infantil o juvenil.
4. **Ejemplos prácticos** para reforzar el aprendizaje.
5. **Ideas narrativas o emocionales** que puedan inspirar la letra de una canción (personajes, metáforas, situaciones, mensajes clave, etc.)

Elige un tema educativo apropiado (ciencia, matemáticas, valores, hábitos saludables, historia, lenguaje, etc.) y genera la lección siguiendo exactamente la estructura anterior.

Mantén un tono positivo, creativo y fácil de musicalizar.
"""

key = os.getenv("GEMINI_API_KEY")

def get_lesson_from_model(query):

    # Inicializa el cliente con tu API key
    client = genai.Client(api_key=key)

    # Envía una consulta (prompt)
    response = client.chat.completions.create(
        model="gpt-4.1-mini", # cambiar a gemini --> mirar chatty
        messages=[
                {"role": "system", "content": BASE_PROMPT},
                {"role": "user", "content": query}
        ]
    )

    # Imprime la respuesta del modelo
    return response.choices[0].message.content




    return {
        "id": 1,
        "name": "Lección de ejemplo",
        "description": "Esto sería una descripción real."
    }