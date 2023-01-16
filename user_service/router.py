import uuid

from fastapi import APIRouter, status, HTTPException, Depends
from schemas import User, PostUser
import mapper
import services
import utils

router = APIRouter(
    tags=['Users'],
    prefix='/users'
)


@router.get(
    '/',
    status_code=200,
    response_model=list[User],
)
@utils.trace_it(tag='router', value='Get users')
async def get_all_users():
    users = await services.get_all_users()
    output = [
        mapper.mapping_model_schema(user)
        for user in users
    ]
    return output


@router.post(
    '/add',
    status_code=201,
    response_model=User
)
@utils.trace_it(tag='router', value='Adding user')
async def add_new_user(user: PostUser):
    user = await services.create_user(user)
    return mapper.mapping_model_schema(user)


@router.delete(
    '/delete/{user_uuid}',
    status_code=status.HTTP_200_OK
)
@utils.trace_it(tag='router', value='Delete user')
async def delete_user(user_uuid: uuid.UUID):
    await services.delete_user(user_uuid)


@router.put(
    '/put/{user_uuid}',
    status_code=status.HTTP_200_OK
)
@utils.trace_it(tag='router', value='Update user')
async def update_user(user_uuid: uuid.UUID, user: PostUser):
    await services.update_user(user_uuid, user)
    user_update = await services.get_user_by_id(user_uuid)
    return mapper.mapping_model_schema(user_update)


@router.put(
    '/update_role/{user_uuid}',
    status_code=status.HTTP_200_OK
)
@utils.trace_it(tag='router', value='Update role')
async def update_role(user_uuid: uuid.UUID, role):
    return await services.update_role(user_uuid, role)
