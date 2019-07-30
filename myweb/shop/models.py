
# Create your models here.
# shop/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator	
from django.utils.html import escape
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    gender = (
        ("male", '男'),
        ("female", '女')
    )
    phone_reg = RegexValidator(r'^09\d{2}-?\d{3}-?\d{3}$',"Please enter valid Taiwanese phone number.")
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    sex = models.CharField(max_length=10,choices=gender)
    phone = models.CharField(max_length=20, validators=[phone_reg])

    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField(blank=True)
    post_photo = models.ImageField(null=True, blank=True, upload_to='photos/', default = 'photos/TV.jpg')
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_less = models.TextField(blank=True)
    # def __str__(self):
    #     return self.post_title
  


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(null=True, blank=True, upload_to='photos/', default = 'photos/TV.jpg')
    remain_product = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name
    def update_remain(self, number):
        if number > int(self.remain_product):
            return False
        else:
            self.remain_product-=number
            self.save()
            return True

# shop/models.py
class ShoppingCar(models.Model):
    client = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,)
    count = models.IntegerField(default=0, validators=[MinValueValidator(1)])
    def __str__(self):
        return self.client.name + self.count + "products"
    def price(self):
        return self.product.product_price * self.count  

