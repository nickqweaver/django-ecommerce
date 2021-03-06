from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def get_product_ids(self):
        products = self.products.all()
        product_ids = []
        for product in products:
            product_ids.append(product.id)
        return product_ids

    def __str__(self):
        return self.name
