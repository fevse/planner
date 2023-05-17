from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Event title",
                "image": "https://forexample.com/image.png",
                "description": "Brief description of this event",
                "tags": ["python", "fastapi", "database", "tests"],
                "location": "Planet Earth"
            }
        }
    
    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Event title",
                "image": "https://forexample.com/image.png",
                "description": "Brief description of this event",
                "tags": ["python", "fastapi", "database", "tests"],
                "location": "Planet Earth"
            }
        }
