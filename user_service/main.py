import time
import logging

from fastapi import FastAPI
import mongoengine

from prometheus_fastapi_instrumentator import Instrumentator

from router import router
from auth.router import router as a_router
from deps import init_tracer


DB_NAME = 'mydb'


logger = logging.getLogger(__name__)
app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Connected to base")
    mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)
    init_tracer()
    Instrumentator().instrument(app).expose(app)


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
