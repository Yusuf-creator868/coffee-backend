from .models import *
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):

      class Meta:
            model = Menu
            fields = ['id', 'choose', 'image', 'name', 'cost']


class CategorySerializer(serializers.ModelSerializer):
      menues = MenuSerializer(many=True, read_only = True)
      class Meta:
            model = Category
            fields = ['id', 'name', "menues"]


class CategoryNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", 'slug']


class CartItemSerializer(serializers.ModelSerializer):
     menus = MenuSerializer(read_only = True)
     total = serializers.SerializerMethodField()
     class Meta:
          model = CartItems
          fields = ['id', 'menus', 'quantity', 'total']
 
     def get_total(self, cartitems):
          cost = cartitems.menus.cost * cartitems.quantity
          return cost
          
      

class CartSerializer(serializers.ModelSerializer):
     items = CartItemSerializer(read_only = True, many=True)
     sum_total = serializers.SerializerMethodField()
     num_of_items = serializers.SerializerMethodField()
     class Meta:
          model = Cart
          fields = ['id', 'cart_code', 'items', 'sum_total', "num_of_items"]
      
     def get_sum_total(self, cart):
         items = cart.items.all()
         total = sum([item.menus.cost * item.quantity for item in items])
         return total
     
     def get_num_of_items(self, cart):
          items = cart.items.all()
          total = sum([item.quantity for item in items])
          return total