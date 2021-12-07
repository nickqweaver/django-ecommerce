from customer.graphql.types import AddressInput, AddressType
from customer.models import STATE_CHOICES
from graphql import GraphQLError
from django.contrib.auth import get_user_model, authenticate
from order.models import OrderItem, Order
from graphene import ObjectType, String, ID, Boolean, Mutation, Field, NonNull
from customer.models import Address
import graphql_jwt
from graphql_jwt.shortcuts import get_token

'''
  The token needs to be stored in session storage on the frontend but for security needs
  to be re generated on refresh and when new tabs are opened. See https://hasura.io/blog/best-practices-of-using-jwt-with-graphql/
  We then can use Apollo client to pass the token via HTTP auth headers and then utilize the decorators from the jwt graphql lib
  to verify tokens are valid before orders are created. Note this does not login/logout users it simply authenticate them so
  will still need to login/logout/authenticate via django auth but also manipulate the token. Need to generate new tokens before they expire
  silently for better UX. 
'''

def is_authenticated(user):
    if user.is_anonymous:
        return False
    else:
      return True
        
class CreateCustomer(Mutation):
  user_id = ID()
  success = Boolean()
  token = String()
  class Arguments:
    username = String(required=True)
    password = String(required=True)
    email = String(required=True)

  def mutate(root, info, username, password, email):
    is_already_user = get_user_model().objects.filter(username=username).exists()
    user_id = None
    token = None
    success = False

    if is_already_user:
      return GraphQLError("Username is already in use")
    else:
      try:
        user = get_user_model()(username=username, email=email)
        user.set_password(password)
        user.save()
        token = get_token(user)
        success = True
        user_id = user.id
      except:
        return GraphQLError("There was an error creating your account")

    return CreateCustomer(user_id=user_id, success=success, token=token)

class UpdateAddress(Mutation):
  success = Boolean()

  class Arguments:
    user_id = ID()
    address = AddressInput()

  def mutate(root, self, address, id):
    user_profile = get_user_model().objects.get(pk=id).profile
       
    return UpdateAddress(success=True)

class Login(Mutation):
  success = Boolean()
  token = String()
  class Arguments:
    username = NonNull(String)
    password = NonNull(String)
  
  def mutate(root, info, username, password):
    try:
      user = authenticate(username=username, password=password)
      token = get_token(user)
    except:
        raise GraphQLError("You entered the wrong username or password")
  
    return Login(success=True, token=token)


class CreateAddress(Mutation):
  success = Boolean()
  address = Field(AddressType)

  class Arguments:
    address = AddressInput()
    user_id = ID()

  def mutate(root, info, address, user_id):
    new_address = None
    success = True
    try:
      ## TODO - get_or_create will always create new even if everything is the same except 1 field. 
      ## Should handle this better by checking if the address object has comparable values and update instead of create
      profile = get_user_model().objects.get(pk=user_id).profile
      new_address, created = Address.objects.get_or_create(profile=profile, address1=address.line_1, address2=address.line_2, zip_code=address.zip, state=address.state, city=address.city, country=address.country)
    except:
      success = False
      raise Exception("Could not add address to profile")

    return CreateAddress(success=success, address=new_address)



class CustomerMutations(ObjectType):
  create_customer = CreateCustomer.Field()
  create_address = CreateAddress.Field()
  update_address = UpdateAddress.Field()
  login = Login.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

 