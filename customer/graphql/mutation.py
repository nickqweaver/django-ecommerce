from graphql import GraphQLError
from django.contrib.auth import get_user_model, authenticate, login, logout
from order.models import OrderItem, Order
from graphene import ObjectType, String, ID, Boolean, Mutation


class CreateCustomer(Mutation):
  user_id = ID()
  success = Boolean()
  
  class Arguments:
    username = String(required=True)
    password = String(required=True)
    email = String(required=True)

  def mutate(root, info, username, password, email):
    is_already_user = get_user_model().objects.filter(username=username).exists()
    
    if is_already_user:
      return GraphQLError("Username is already in use")
    else:
      user = get_user_model()(username=username, email=email)
      user.set_password(password)
      user.save()
    
    return CreateCustomer(user_id=user.id, success=True)


class CustomerMutations(ObjectType):
  create_customer = CreateCustomer.Field()