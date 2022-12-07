import mongoengine


class Movie(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'products',
    }

    movie_uuid = mongoengine.UUIDField(primary_key=True)
    name = mongoengine.StringField(max_length=200, required=True)
    description = mongoengine.StringField(max_length=800, required=True)
    price = mongoengine.IntField(required=True)
    rating = mongoengine.IntField(required=False)
    year = mongoengine.IntField(required=True)
