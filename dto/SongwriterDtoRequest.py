from pydantic import BaseModel, Field


class SongwriterDtoRequest(BaseModel):
    # Informacion de Teacher
    main_concept: str = Field(..., min_length=3)
    secondary_theme: str = Field(..., min_length=3)

    # Informacion de Prompt Splitter
    learning_theme: str = Field(..., min_length=3)
    user_information: str = Field(..., min_length=3)
    musical_preferences: str = Field(..., min_length=3) # Posiblemente fuera 
