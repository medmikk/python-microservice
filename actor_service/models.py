import mongoengine


class Actor(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'actors',
    }

    actor_uuid = mongoengine.UUIDField(primary_key=True)
    name = mongoengine.StringField(max_length=200, required=True)
    description = mongoengine.StringField(max_length=800, required=True)
    birthday = mongoengine.StringField(max_length=10, required=True)
