from pydantic import BaseModel, Field

class SongwriterDtoReply(BaseModel):
    lyrics: str = Field(..., min_length=3)
