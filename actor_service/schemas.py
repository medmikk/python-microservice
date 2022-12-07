from pydantic import BaseModel
import uuid


class PostActor(BaseModel):
    name: str
    description: str
    birthday: str


class Actor(PostActor):
    actor_uuid: uuid.UUID

    class Config:
        orm_mode = True
