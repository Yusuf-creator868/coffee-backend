from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
      name = models.CharField(max_length=50)
      slug = models.SlugField(blank=True, null=True)

      def __str__(self):
            return self.name
      
      def save(self, *args, **kwargs):
            if not self.slug:
                  self.slug = slugify(self.name)
            super().save(*args, **kwargs)


class Menu(models.Model):
      choose = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menues')
      image = models.ImageField(upload_to='img', null=True)
      name = models.CharField(max_length=100, null=True)
      cost = models.DecimalField(max_digits=10, decimal_places=0)

      def __str__(self):
            return self.name
      

class Cart(models.Model):
      cart_code = models.CharField(max_length=11, unique= True)

      def __str__(self):
            return self.cart_code
      

class CartItems(models.Model):
      cart_code = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
      menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
      quantity = models.IntegerField(default = 1)

      def __str__(self):
            return f"{self.quantity} * {self.menus.name} in favcart {self.cart_code.id}"



