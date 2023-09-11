from pydantic import BaseModel, Field

class LoginEntity(BaseModel):
    id: int
    username: str = Field(..., min_length=4) 
    password: str 