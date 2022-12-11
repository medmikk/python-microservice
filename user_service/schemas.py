from pydantic import BaseModel
import uuid


class PostUser(BaseModel):
    name: str
    password: str
    email: str


class User(PostUser):
    user_uuid: uuid.UUID

    class Config:
        orm_mode = True
