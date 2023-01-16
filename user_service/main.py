import logging

from fastapi import FastAPI
import mongoengine
from prometheus_client import Summary, Counter

import aio_pika

from broker.consumer import on_message

from prometheus_fastapi_instrumentator import Instrumentator

from router import router
from auth.router import router as a_router
from deps import init_tracer


DB_NAME = 'mydb'


logger = logging.getLogger(__name__)
app = FastAPI()

logger = logging.getLogger(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
total_requests = Counter('total_requests', 'Total requests counter')
total_service_requests = Counter('total_service_requests', 'Total service requests counter')
service_endpoints = ('/metrics', '/_health')


@app.on_event("startup")
async def startup():
    logger.info("Connected to base")
    mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)
    init_tracer()
    Instrumentator().instrument(app).expose(app)

    connection = await aio_pika.connect("amqp://guest:guest@rabbitmq:5672/")
    channel = await connection.channel()

    queue = await channel.declare_queue("fastapi_task")

    await queue.consume(on_message, no_ack=True)


@app.on_event("shutdown")
async def shutdown():
    logger.info("Disconnected to base")
    mongoengine.disconnect(alias=DB_NAME)


@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }


app.include_router(router, prefix='/v1')
app.include_router(a_router, prefix='/v1')
