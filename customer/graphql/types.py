
import graphene
from graphene import String, Int
from graphene_django import DjangoObjectType
from customer.models import Address, Profile, Customer

class AddressInput(graphene.InputObjectType):
    line_1 = String(required=True)
    line_2 = String()
    city = String(required=True)
    zip = Int(required=True)
    # state = Field(Enum('State', STATE_CHOICES)) TODO - Change back to Enums later, passes value and we need the enum member to store in db
    # country = Field(Enum('Country_Code', COUNTRIES))
    state = String(required=True)
    country = String(required=True)

class AddressType(DjangoObjectType):
  class Meta:
    model = Address

class ProfileType(DjangoObjectType):
  class Meta:
    model = Profile

class CustomerType(DjangoObjectType):

  class Meta:
    model = Customer