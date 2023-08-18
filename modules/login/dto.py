from pydantic import BaseModel, Field

class LoginDTO(BaseModel):
    username: str = Field(..., min_length=4)
    password: str