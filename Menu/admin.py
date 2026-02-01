from django.contrib import admin
from .models import *

admin.site.register([Category, Menu, Cart, CartItems])
# Register your models here.
