from pydantic import BaseModel, Field

class LoginDTO(BaseModel):
    id: int 
    username: str = Field(..., min_length=4)
    password: str