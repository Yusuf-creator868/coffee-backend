from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_menu(request):
      serializer = MenuSerializer(data = request.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_item(request):
      

      code = request.data.get('code')
      menu_id = request.data.get('menu_id')

      cart, created = Cart.objects.get_or_create(cart_code = code)
      menuid = Menu.objects.get(id = menu_id)

      cartitem, created = CartItems.objects.get_or_create(cart_code = cart, menus = menuid)
      cartitem.quantity = 1
      cartitem.save()

      serializer = CartItemSerializer(cartitem)

      return Response({"data": serializer.data, "message": "Item was added successfully!"})

@api_view(["GET"])
def product_in_cart(request):
      code = request.query_params.get('code')
      menu_id = request.query_params.get('menu_id')

      cart = Cart.objects.get(cart_code = code)
      menu = Menu.objects.get(id = menu_id)

      product_exists_in_card = CartItems.objects.filter(cart_code = cart, menus = menu).exists()

      return Response({'product_in_cart': product_exists_in_card})




@api_view(['GET'])
def get_cart(request):
      cart_code = request.query_params.get('code')
      cart = Cart.objects.get(cart_code = cart_code)
      serializer = CartSerializer(cart)
      return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_items(request, pk):
      delete = CartItems.objects.get(id = pk)
      delete.delete()
      return Response({"message": "Deleted successfully!"})






@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_category(request):
      serializer = CategoryNamesSerializer(data = request.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
@permission_classes([AllowAny])
def get_menu(request, slug):
      menu = get_object_or_404(Category, slug=slug)
      serializer = CategorySerializer(menu)
      return Response(serializer.data)



@api_view(["GET"])
@permission_classes([AllowAny])
def get_category(request):
      category = Category.objects.all()
      serializers = CategoryNamesSerializer(category, many = True)
      return Response(serializers.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_menu(request, pk):
      rem_menu = Menu.objects.get(id = pk)
      rem_menu.delete()
      return Response("Deleted!")

# Create your views here.


def home(request):
    return JsonResponse({"status": "Backend is running 🚀"})


