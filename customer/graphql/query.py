from graphene import List, Field, ObjectType, Field
from customer.graphql.types import ProfileType, CustomerType
from graphql_jwt.decorators import login_required

class CustomerQuery(ObjectType):
  get_customer_profile = Field(ProfileType)
  get_customer = Field(CustomerType)

  @login_required
  def resolve_get_customer_profile(self, info):
    profile = info.context.user.profile
    return profile

  @login_required
  def resolve_get_customer(self, info):
    user = info.context.user
    return user


