import graphene
from graphene_django.types import ObjectType
from graphql.type.definition import GraphQLResolveInfo
from .types import ActorType, MovieType
from ..models import Actor, Movie
from typing import Optional, List


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.ID(required=True))
    movie = graphene.Field(MovieType, id=graphene.ID(required=True))

    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)

    def resolve_actor(self, info: GraphQLResolveInfo, **kwargs) -> Optional[Actor]:
        id_ = kwargs.get('id')

        if id_ is not None:
            return Actor.objects.filter(pk=id_).first()
        return None

    def resolve_movie(self, info: GraphQLResolveInfo, **kwargs) -> Optional[Movie]:
        id_ = kwargs.get('id')

        if id_ is not None:
            return Movie.objects.filter(pk=id_).first()
        return None

    def resolve_actors(self, info: GraphQLResolveInfo, **kwargs) -> List[Actor]:
        return Actor.objects.all()

    def resolve_movies(self, info: GraphQLResolveInfo, **kwargs) -> List[Movie]:
        return Movie.objects.all()
