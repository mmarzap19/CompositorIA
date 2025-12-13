import json

dataset = json.load(open("dataset.json"))

output = []

for item in dataset:
    main_concept = item["main_concept"]
    secondary_theme = item["secondary_theme"]
    learning_theme = item["learning_theme"]
    user_information = item["user_information"]
    musical_preferences = item["musical_preferences"]
    song_lyrics = item["song_lyrics"]

    prompt_completion_example = {
        "prompt": [
            {
                "role": "user",
                "content": (
                    "Genera una canción con la siguiente información:\n\n"
                    f"main_concept: {main_concept}\n"
                    f"secondary_theme: {secondary_theme}\n"
                    f"learning_theme: {learning_theme}\n"
                    f"user_information: {user_information}\n"
                    f"musical_preferences: {musical_preferences}\n\n"
                    "Escribe la canción completa."
                )
            }
        ],
        "completion": [
            {
                "role": "assistant",
                "content": song_lyrics
            }
        ]
    }

    output.append(prompt_completion_example)

json.dump(output, open("prompt_completion_dataset.json", "w"), ensure_ascii=False, indent=2)
