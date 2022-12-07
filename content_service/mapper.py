import schemas
import models


def mapping_model_schema(model: models.Movie):
    schema = schemas.Movie(
        movie_uuid=model.movie_uuid,
        name=model.name,
        description=model.description,
        price=model.price,
        rating=model.rating,
        year=model.year,
    )
    return schema


def mapping_model_schema(schema: schemas.Movie):
    schema = schemas.Movie(
        movie_uuid=schema.movie_uuid,
        name=schema.name,
        description=schema.description,
        price=schema.price,
        rating=schema.rating,
        year=schema.year,
    )
    return schema