from pydantic import BaseModel, Field

class LoginEntity(BaseModel):
    username: str = Field(..., min_length=4) 
    password: str 