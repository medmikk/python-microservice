from pydantic import BaseModel
import uuid


class BuySub(BaseModel):
    qiwi: str
    sub_type: str
    uuid: str


class Sub(BuySub):
    class Config:
        orm_mode = True
