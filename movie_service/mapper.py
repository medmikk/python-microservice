import schemas
import models
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import opentracing


def mapping_model_schema(model: models.Movie):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_model_schema.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            try:
                schema = schemas.Movie(
                    movie_uuid=model.movie_uuid,
                    name=model.name,
                    description=model.description,
                    price=model.price,
                    rating=model.rating,
                    year=model.year,
                    actors=model.actors,
                    sub_type=model.sub_type
                )
                return schema
            except Exception as e:
                span.set_tag('error', e.__name__)
                span.log_kv({'event': mapping_model_schema.__name__, 'value': e.__name__})


def mapping_schema_model(schema: schemas.Movie):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_schema_model.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            try:
                model = schemas.Movie(
                    movie_uuid=schema.movie_uuid,
                    name=schema.name,
                    description=schema.description,
                    price=schema.price,
                    rating=schema.rating,
                    year=schema.year,
                    actors=schema.actors,
                    sub_type=schema.sub_type
                )
                return model
            except Exception as e:
                span.set_tag('error', e.__name__)
                span.log_kv({'event': mapping_schema_model.__name__, 'value': e.__name__})
