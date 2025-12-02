# service/lesson_service.py
from openai import OpenAI

key = ""

def get_lesson_from_model(query):
    # Aquí pondrías tu lógica real


    # Inicializa el cliente con tu API key
    client = OpenAI(api_key= key)

    # Envía una consulta (prompt)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
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