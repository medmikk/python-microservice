from models import User
import schemas
import uuid
import utils


@utils.trace_it(tag='service', value='Get all users')
async def get_all_users() -> list[User]:
    return User.objects


@utils.trace_it(tag='service', value='Create user')
async def create_user(user: schemas.PostUser) -> User:
    if await get_user_by_username(user.email) is None:
        user = User(
            user_uuid=uuid.uuid4(),
            name=user.name,
            password=user.password,
            email=user.email,
            role=user.role
        ).save()
        return user
    else:
        return await get_user_by_username(user.email)


@utils.trace_it(tag='service', value='Delete user')
async def delete_user(user_uuid):
    return User.objects(user_uuid=user_uuid).delete()


@utils.trace_it(tag='service', value='Update user')
async def update_user(user_uuid, user_update: schemas.PostUser):
    return User.objects(user_uuid=user_uuid).first().update(name=user_update.name,
                                                            password=user_update.password,
                                                            email=user_update.email,
                                                            role=user_update.role)


@utils.trace_it(tag='service', value='Get user by username')
async def get_user_by_username(input_email: str) -> User:
    return User.objects(email=input_email).first()


@utils.trace_it(tag='service', value='Update role by id')
async def update_role(user_uuid, role):
    return User.objects(user_uuid=user_uuid).update(role=role)


@utils.trace_it(tag='service', value='Get user by id')
async def get_user_by_id(user_uuid):
    return User.objects(user_uuid=user_uuid).first()
