from flask import Flask, jsonify, request, send_file
from service.musician_service import get_audio_from_model
from service.teacher_service import get_lesson_from_model
# from service.musician_service import get_audio_from_model

app  = Flask(__name__)

@app.route('/')
def root():
    return "root"

@app.route('/get_lesson')
def get_lesson():
    data = request.get_json()

    # Obtenemos el json de la petición
    query = data["learning_theme"]

    # Enviamos a chatGPT la petición y obtenemos la lección
    a= get_lesson_from_model(query)

    # Enviamos la leccion al usuario
    return a

@app.route('/get_lyrics')
def get_lyrics():
    return "I am a lyrics"

@app.route('/get_audio')
def get_audio():
    data = request.get_json()

    # Obtenemos el json de la petición
    query = data["lyrics"]

    # Enviamos a suno la petición y obtenemos el audio
    # Generar audio y guardarlo en el equipo
    audio_path = get_audio_from_model(query)

    # Devolver el archivo como respuesta
    return send_file(audio_path, mimetype="audio/mpeg")


@app.route('/generate_song')
def generate_song():
    return "I am a song"

'''
@app.route("/users/<user_id>")
def get_user(user_id):
    user={'id':user_id,'name':'test','telefono':'999-666-333'}
    #/users/2654?query=query_test
    query = request.args.get('query')
    if query: # si existe query
        user['query'] = query
    return jsonify(user), 200 # retornar código 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() # obtener inf del body
    #data["status"] = "user created"
    return jsonify(data), 201 # código 201 (inf ya se creó)


'''
if __name__ == '__main__':
    app.run(debug=True)

