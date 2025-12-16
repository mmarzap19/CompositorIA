# service/audio_service.py
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, Voice, VoiceSettings, voices
import os

'''
available_voices = voices()
for v in available_voices:
    print(v.voice_id, v.name)
'''
load_dotenv()  # carga las vars del archivo .env

key = os.getenv("ELEVENLABS_KEY")

def get_audio_from_model(query, output_path="/utils/lesson_audio.mp3"):
    
    # Inicializa el cliente con tu API key
    client = ElevenLabs(api_key= key)

    # Envía una consulta (prompt)
    audio_generator = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",
        model_id="eleven_turbo_v2",
        text=query,
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.4,
            use_speaker_boost=True
        )
    )

    # Guardar el audio en el equipo
    with open(output_path, "wb") as f:
        for chunk in audio_generator:     # ElevenLabs devuelve chunks (stream)
            f.write(chunk)

    return output_path   # devolvemos la ruta del archivo guardado
