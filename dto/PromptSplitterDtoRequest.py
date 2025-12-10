from pydantic import BaseModel, Field

class PromptSplitterDtoRequest(BaseModel):
    user_prompt: str = Field(..., min_length=3)