import graphene
from .movie_mutation import CreateMovie, UpdateMovie, DeleteMovie
from .actor_mutation import CreateActor, UpdateActor, DeleteActor


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    delete_actor = DeleteActor.Field()

    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
