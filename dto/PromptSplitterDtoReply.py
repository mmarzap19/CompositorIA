from pydantic import BaseModel, Field

class PromptSplitterDtoReply(BaseModel):
    learning_theme: str = Field(..., min_length=3)
    user_information: str = Field(..., min_length=3)
    musical_preferences: str = Field(..., min_length=3)