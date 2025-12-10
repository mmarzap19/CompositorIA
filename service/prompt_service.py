from dotenv import load_dotenv
import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
load_dotenv()  # carga las vars del archivo .env

# Si tu webhook requiere autenticación básica
N8N_USER = os.getenv("N8N_USER", None)
N8N_PASSWORD = os.getenv("N8N_PASSWORD", None)

# URL del webhook en tu instancia local
N8N_WEBHOOK_URL = "https://localhost:5678/webhook-test/promp-splitter"


def send_text_to_n8n(query):
    auth = (N8N_USER, N8N_PASSWORD) if N8N_USER and N8N_PASSWORD else None

    response = requests.post(
        N8N_WEBHOOK_URL,
        json={"text": query},
        auth=auth
    )

    response.raise_for_status()  # lanza error si n8n devuelve error
    return response.json()       # o response.content si devuelve binario


@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "Falta 'query' en la petición"}), 400

    result = send_text_to_n8n(query)
    return jsonify({"n8n_response": result})


if __name__ == "__main__":
    app.run(debug=True)
