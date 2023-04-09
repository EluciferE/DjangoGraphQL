import graphene
from graphql.type.definition import GraphQLResolveInfo
from ..types import Actor, ActorType, Movie, MovieType, MovieInput


class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    status = graphene.Boolean()
    movie = graphene.Field(MovieType)

    def __init__(self, status, movie):
        self.status = status
        self.movie = movie

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, input: MovieInput = None):
        actor_ids = [actor_input.id for actor_input in input.actors]
        actors = [Actor.objects.filter(id__in=actor_ids)]

        if len(actors) != len(actor_ids):
            return CreateMovie(status=False, movie=None)

        movie_instance = Movie(
            title=input.title,
            year=input.year
        )
        movie_instance.save()
        movie_instance.actors.set(actors)

        return CreateMovie(status=True, movie=movie_instance)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    status = graphene.Boolean()
    movie = graphene.Field(MovieType)

    def __init__(self, status, movie=None):
        self.status = status
        self.movie = movie

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, input: MovieInput = None):
        movie_instance = Movie.objects.filter(id=input.id).first()
        if movie_instance is None:
            return UpdateMovie(status=False)

        actor_ids = [actor_input.id for actor_input in input.actors]
        actors = Actor.objects.filter(id__in=actor_ids)

        if len(actors) != len(actor_ids):
            return UpdateMovie(status=False)

        if input.title:
            movie_instance.title = input.title
        if input.year:
            movie_instance.year = input.year

        movie_instance.save()

        if input.actors:
            movie_instance.actors.set(actors)

        return UpdateMovie(status=True, movie=movie_instance)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.Boolean()

    def __init__(self, status):
        self.status = status

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, id: int):
        movie_instance = Movie.objects.filter(pk=id).first()
        if movie_instance is None:
            return DeleteMovie(status=False)

        movie_instance.delete()
        return DeleteMovie(status=True)