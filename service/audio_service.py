# service/audio_service.py

key = ""

def get_audio_from_model(query):
    return query
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

