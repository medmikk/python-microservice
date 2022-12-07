from pydantic import BaseModel
import uuid


class PostMovie(BaseModel):
    name: str
    description: str
    price: int
    rating: int
    year: int
    # actors: list[str]


class Movie(PostMovie):
    movie_uuid: uuid.UUID

    class Config:
        orm_mode = True
