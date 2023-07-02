from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
    

class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    review = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    

