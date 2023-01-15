import uuid

import schemas
import models
import utils


@utils.trace_it_sync("mapper", value="model -> schema")
def mapping_model_schema(model: models.User):
    schema = schemas.User(
        user_uuid=model.user_uuid,
        name=model.name,
        email=model.email,
        password=model.password,
        role=model.role
    )
    return schema


@utils.trace_it_sync("mapper", value="schema -> model")
def mapping_schema_model(schema: schemas.User):
    model = schemas.User(
        actor_uuid=schema.user_uuid,
        name=schema.name,
        password=schema.password,
        email=schema.email,
        role=schema.role
    )
    return model
