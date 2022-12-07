from models import Actor
import schemas
import uuid


async def get_all_actors() -> list[Actor]:
    return Actor.objects


async def create_actor(actor: schemas.PostActor) -> Actor:
    mov = Actor(
        actor_uuid=uuid.uuid4(),
        name=actor.name,
        description=actor.description,
        birthday=actor.birthday,
    ).save()
    return mov
