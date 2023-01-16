import pydantic
import uuid
import json
import aio_pika


class PostRole(pydantic.BaseModel):
    command: str = 'post'
    user_id: str
    role: str


async def send_rabbitmq(msg: PostRole):
    connection = await aio_pika.connect('amqp://guest:guest@rabbitmq:5672/')

    channel = await connection.channel()

    await channel.default_exchange.publish(
        aio_pika.Message(json.dumps(msg.dict()).encode("utf-8")),
        routing_key="fastapi_task"
    )

    await connection.close()