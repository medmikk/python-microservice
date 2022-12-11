from models import Movie
import schemas
import uuid
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import opentracing


async def get_all_movies() -> list[Movie]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return Movie.objects


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
            ).save()
            return mov
