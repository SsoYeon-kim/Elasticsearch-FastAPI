from datetime import date
from typing import List
from pydantic import BaseModel


class Post(BaseModel):
    """Pydantic model for post documents."""

    display_tag: str
    # id: str
    image_url: str
    published_at: date
    reading_time: float
    subtitle: str
    tags: List[str]
    title: str
    url: str

    class Config:
        orm_mode = True