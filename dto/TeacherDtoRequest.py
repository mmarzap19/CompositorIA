from pydantic import BaseModel, Field


class TeacherDtoRequest(BaseModel):
    learning_theme: str = Field(..., min_length=3)
