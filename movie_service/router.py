from fastapi import APIRouter, status, HTTPException, Depends
from schemas import Movie, PostMovie
import mapper
import services
import logging
import opentracing
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context

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
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
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
    tracer = opentracing.global_tracer()
    with tracer.start_span(add_new_movie.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mov = await services.create_movie(movie)
            return mov


@router.get(
    '/movie',
    status_code=200,
    response_model=Movie,
)
async def get_movie_by_id(movie_id, user_sub: str):
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            movie = await services.get_movie(movie_id, user_sub)
            output = mapper.mapping_model_schema(movie)
            return output


@router.delete(
    '/delete',
    status_code=200
)
async def delete_movie(movie_id):
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_movies.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            await services.delete_movie(movie_id)
