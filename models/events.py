from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "Event title",
                "image": "https://forexample.com/image.png",
                "description": "Brief description of this event",
                "tags": ["python", "fastapi", "database", "tests"],
                "location": "Planet Earth"
            }
        }


class EventUpdate(SQLModel):
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
