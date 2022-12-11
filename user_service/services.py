from models import User
import schemas
import uuid
import utils


@utils.trace_it(tag='service', value='Get user by username')
async def get_all_users() -> list[User]:
    return User.objects


@utils.trace_it(tag='service', value='Get user by username')
async def create_user(user: schemas.PostUser) -> User:
    user = User(
        user_uuid=uuid.uuid4(),
        name=user.name,
        password=user.password,
        email=user.email,
    ).save()
    return user


@utils.trace_it(tag='service', value='Get user by username')
async def get_user_by_username(input_email: str) -> User:
    return User.objects(email = input_email).first()