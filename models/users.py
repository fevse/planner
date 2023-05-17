from typing import Optional, List

from pydantic import BaseModel, EmailStr
from beanie import Document, Link

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "forexample@fastapi.com",
                "password": "qwerty",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
