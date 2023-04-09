import graphene
import MoviesAPI.schema


class Query(MoviesAPI.schema.Query, graphene.ObjectType):
    pass


class Mutation(MoviesAPI.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
