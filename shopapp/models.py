from django.db import models
from django.utils.text import slugify
from decimal import Decimal
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/',null=True,blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
from decimal import Decimal

class DiscountProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    d_rate = models.IntegerField(default=0)
    d_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True, null=True)
    image1 = models.ImageField(upload_to='disscountProducts_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='discountProducts_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='discountProducts_images/', null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        discount_rate_decimal = Decimal(self.d_rate) / 100  
        if 0 <= discount_rate_decimal <= 1: 
            self.d_price = self.price * (1 - discount_rate_decimal)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='products_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products_images/', null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    



    