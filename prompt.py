generar_cancion_didactica = {
    "name": "generar_cancion_didactica",
    "description": (
        "Genera la letra de una canción didáctica en español a partir de un contenido que se quiere aprender. "
        "La canción está pensada para un público concreto (por ejemplo, profesionales sanitarios), pero NUNCA debe incluir "
        "ni repetir datos personales del usuario. Esa información solo sirve para adaptar el tono, el nivel de detalle "
        "y el tipo de metáforas.\n\n"
        "La salida debe ser SIEMPRE un objeto JSON con tres claves de alto nivel: "
        "ESTROFA, PUENTE y ESTRIBILLO.\n\n"
        "- ESTROFA: introduce el CONCEPTO_PRINCIPAL y sitúa el contexto, explicando los primeros pasos o ideas clave.\n"
        "- PUENTE: conecta la explicación inicial con el mensaje central, enfatizando transiciones, matices y posibles dudas.\n"
        "- ESTRIBILLO: resume y refuerza los puntos más importantes de forma repetitiva, fácil de recordar y emocional.\n\n"
        "En cada parte, desglosa los temas principales que se quieren aprender (CONCEPTO_PRINCIPAL, SUBTEMA1, SUBTEMA2) "
        "usando lenguaje claro, imágenes mentales sencillas y recursos propios de la música pop (ritmo, repetición, contraste), "
        "pensados para facilitar la memorización del contenido didáctico."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "ESTROFA": {
                "type": "string",
                "description": (
                    "Primera parte de la canción. Presenta el CONCEPTO_PRINCIPAL y enmarca la situación de aprendizaje. "
                    "Debe introducir los temas clave de forma narrativa y comprensible, sin incluir datos personales del usuario. "
                    "Organiza las ideas de manera secuencial para que se entienda el punto de partida y el problema o necesidad "
                    "que se quiere abordar."
                )
            },
            "PUENTE": {
                "type": "string",
                "description": (
                    "Sección de transición que une la ESTROFA con el ESTRIBILLO. "
                    "Profundiza en SUBTEMA1 y SUBTEMA2, aclarando dudas habituales, errores frecuentes o matices importantes. "
                    "Su función es preparar al oyente para el mensaje central del ESTRIBILLO, manteniendo un tono motivador "
                    "y didáctico, sin mencionar datos personales."
                )
            },
            "ESTRIBILLO": {
                "type": "string",
                "description": (
                    "Parte central y más repetitiva de la canción. Resume los aprendizajes clave de forma clara y pegadiza. "
                    "Debe recoger el CONCEPTO_PRINCIPAL y los puntos más importantes de SUBTEMA1 y SUBTEMA2 en frases cortas, "
                    "memorables y emocionales. Es la sección que el oyente debería recordar fácilmente, y nunca debe contener "
                    "datos personales ni referencias directas a la identidad del usuario."
                )
            }
        },
        "required": ["ESTROFA", "PUENTE", "ESTRIBILLO"]
    }
}
