from pydantic import BaseModel

from typing import List


class Event(BaseModel):
    id: int
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
