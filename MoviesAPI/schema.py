import graphene
from .graphql import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
