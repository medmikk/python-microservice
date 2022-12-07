from fastapi import APIRouter, status, HTTPException, Depends
from schemas import Movie, PostMovie
import mapper
import services

router = APIRouter(
    tags=['Movies'],
    prefix='/movies'
)


@router.get(
    '/',
    status_code=200,
    response_model=list[Movie],
)
async def get_all_movies():
    movies = await services.get_all_movies()
    output = [
        mapper.mapping_model_schema(movie)
        for movie in movies
    ]
    return output


@router.post(
    '/add',
    status_code=201,
    response_model=Movie
)
async def add_new_movie(movie: PostMovie):
    mov = await services.create_movie(movie)
    return mov


@router.delete(
    '/{movie_uuid}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_movie(movie_uuid: str):
    raise HTTPException(
        status_code=404,
        detail=f"Not found movie with id {movie_uuid}",
    )

