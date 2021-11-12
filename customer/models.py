from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
from store import settings


STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('MP', 'Northern Mariana Islands'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VI', 'Virgin Islands'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'))
class Customer(AbstractUser):
  pass

class Profile(models.Model):
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")

class Address(models.Model):
    name = CharField(max_length=30, blank=True, default='')
    address1 = models.CharField(max_length=30,)
    address2 = models.CharField(max_length=30, blank=True, default='')
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=5)
    country = models.CharField(
        "Country",
        max_length=3,
    )
    profile = ForeignKey(Profile, related_name='addresses', on_delete=models.CASCADE)


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Customer)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    