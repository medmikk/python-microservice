from fastapi import FastAPI, Request
import mongoengine
from router import router

DB_NAME = 'mydb'

app = FastAPI()


@app.on_event("startup")
async def startup():
    mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


app.include_router(router, prefix='/v1')