import schemas
import models


def mapping_model_schema(model: models.Actor):
    schema = schemas.Actor(
        actor_uuid=model.actor_uuid,
        name=model.name,
        description=model.description,
        birthday=model.birthday,
    )
    return schema


def mapping_schema_model(schema: schemas.Actor):
    model = schemas.Actor(
        actor_uuid=schema.actor_uuid,
        name=schema.name,
        description=schema.description,
        birthday=schema.birthday,
    )
    return model
