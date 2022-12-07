from fastapi import APIRouter, status, HTTPException, Depends
from schemas import Actor, PostActor
import mapper
import services

router = APIRouter(
    tags=['Actors'],
    prefix='/actors'
)


@router.get(
    '/',
    status_code=200,
    response_model=list[Actor],
)
async def get_all_actors():
    actors = await services.get_all_actors()
    output = [
        mapper.mapping_model_schema(actor)
        for actor in actors
    ]
    return output


@router.post(
    '/add',
    status_code=201,
    response_model=Actor
)
async def add_new_actor(actor: PostActor):
    act = await services.create_actor(actor)
    return act


@router.delete(
    '/{actor_uuid}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_actor(actor_uuid: str):
    raise HTTPException(
        status_code=404,
        detail=f"Not found actor with id {actor_uuid}",
    )

