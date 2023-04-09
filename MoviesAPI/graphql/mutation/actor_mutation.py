import graphene
from graphql.type.definition import GraphQLResolveInfo
from ..types import Actor, ActorType, ActorInput


class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    status = graphene.Boolean()
    actor = graphene.Field(ActorType)

    def __init__(self, status, actor):
        self.status = status
        self.actor = actor

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, input: ActorType = None):
        actor_instance = Actor(name=input.name)
        actor_instance.save()
        return CreateActor(status=True, actor=actor_instance)


class UpdateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    status = graphene.Boolean()
    actor = graphene.Field(ActorType)

    def __init__(self, status, actor=None):
        self.status = status
        self.actor = actor

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, input: ActorType = None):
        actor_instance = Actor.objects.filter(id=input.id).first()
        if actor_instance is None:
            return UpdateActor(status=False)

        actor_instance.name = input.name
        actor_instance.save()

        return UpdateActor(status=True, actor=actor_instance)


class DeleteActor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.Boolean()
    actors = graphene.List(ActorType)

    def __init__(self, status, actors=None):
        self.status = status
        self.actors = actors

    @staticmethod
    def mutate(root, info: GraphQLResolveInfo, id: int):
        actor_instance = Actor.objects.filter(pk=id).first()
        if actor_instance is None:
            return DeleteActor(status=False)

        actor_instance.delete()
        actors = Actor.objects.all()
        return DeleteActor(status=True, actors=actors)
