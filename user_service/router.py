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
@utils.trace_it(tag='router', value='get users')
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
@utils.trace_it(tag='router', value='adding user')
async def add_new_user(user: PostUser):
    user = await services.create_user(user)
    return user #TODO mapping


