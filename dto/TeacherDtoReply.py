from pydantic import BaseModel, Field


class TeacherDtoReply(BaseModel):
    main_concept: str = Field(..., min_length=3)
    secondary_theme: str = Field(..., min_length=3)
