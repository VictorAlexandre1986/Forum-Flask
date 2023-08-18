from pydantic import BaseModel, Field

class loginEntity(BaseModel):
    username: str = Field(..., min_length=4) 
    password: str 