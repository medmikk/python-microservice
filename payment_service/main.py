from fastapi import FastAPI, Request
import mongoengine
from router import router
import logging

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Summary, Counter
from deps import init_tracer

DB_NAME = 'mydb'
app = FastAPI()

logger = logging.getLogger(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
total_requests = Counter('total_requests', 'Total requests counter')
total_service_requests = Counter('total_service_requests', 'Total service requests counter')
service_endpoints = ('/metrics', '/_health')


@app.on_event("startup")
async def startup():
    # mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)
    logger.info("Payment start up successfully")
    Instrumentator().instrument(app).expose(app)
    init_tracer()


@app.on_event("shutdown")
async def shutdown():
    # mongoengine.disconnect(alias=DB_NAME)
    logger.info("Payment shut down")


@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }


app.include_router(router, prefix='/v1')
