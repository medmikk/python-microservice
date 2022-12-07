from models import Movie
import schemas
import uuid


async def get_all_movies() -> list[Movie]:
    return Movie.objects


async def create_movie(movie: schemas.PostMovie) -> Movie:
    mov = Movie(
        movie_uuid=uuid.uuid4(),
        name=movie.name,
        description=movie.description,
        price=movie.price,
        rating=movie.rating,
        year=movie.year,
    ).save()
    return mov
