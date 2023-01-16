from models import Movie
import schemas
import uuid
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import opentracing
from fastapi import HTTPException


async def get_all_movies() -> list[Movie]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return Movie.objects


async def get_movie(movie_uuid, user_role: str) -> Movie:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mov: Movie = Movie.objects(movie_uuid=movie_uuid).first()
            if mov.sub_type == 'user' or (mov.sub_type == 'sub1' and user_role != 'user') or (mov.sub_type == 'sub2' and user_role == 'sub2'):
                return mov
            else:
                raise HTTPException(status_code=402, detail='Payment required')


async def create_movie(movie: schemas.PostMovie) -> Movie:
    tracer = opentracing.global_tracer()
    with tracer.start_span(create_movie.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mov = Movie(
                movie_uuid=uuid.uuid4(),
                name=movie.name,
                description=movie.description,
                price=movie.price,
                rating=movie.rating,
                year=movie.year,
                actors=movie.actors,
                sub_type=movie.sub_type
            ).save()
            return mov


async def delete_movie(movie_uuid):
    tracer = opentracing.global_tracer()
    with tracer.start_span(create_movie.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return Movie.objects(movie_uuid=movie_uuid).delete()
