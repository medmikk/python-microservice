import pydantic
import uuid
import enum
import json
import aio_pika
from services import update_role


class PostRole(pydantic.BaseModel):
    command: str
    user_id: uuid.UUID
    role: str


async def on_message(message: aio_pika.IncomingMessage):
    txt = message.body.decode("utf-8")
    msg_info = PostRole(**json.loads(txt))
    if msg_info.command == 'post':
        await set_role(msg_info.user_id, msg_info.role)


async def set_role(uuidr, role):
    await update_role(uuidr, role)
    pass
