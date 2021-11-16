from customer.graphql.types import AddressInput, AddressType
from customer.models import STATE_CHOICES
from graphql import GraphQLError
from django.contrib.auth import get_user_model, authenticate, login, logout
from order.models import OrderItem, Order
from graphene import ObjectType, String, ID, Boolean, Mutation, Field, Int, Enum
from customer.models import Address


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

class UpdateAddress(Mutation):
  success = Boolean()

  class Arguments:
    user_id = ID()
    address = AddressInput()

  def mutate(root, self, address, id):
    user_profile = get_user_model().objects.get(pk=id).profile
    ## Get or Create address object here and add profile to it ?
    ## How do we handle the fact that a user can have multiple address's?
    ## Maybe we have add address mutation and update address mutation, to update address we
    ## would just need to pass the address ID up instead of needing to worry about the user's info
    ## Then if user does not have address we are just simply creating one and attaching their profile
    ## to it.      
    return UpdateAddress(success=True)

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