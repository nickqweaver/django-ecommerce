from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True, default='')
    thumbnail = models.ImageField(blank=True)

    def __str__(self):
        return self.name
