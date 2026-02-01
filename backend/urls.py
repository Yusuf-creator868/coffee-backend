"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import CusromRefreshTokenView, CustomTokenObtainPairView, logout, register, is_authenticated
from django.conf import settings
from django.conf.urls.static import static
from Menu.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CusromRefreshTokenView.as_view(), name="token_refresh"),
    path("logout/", logout, name="logout"),
    path("register/", register),
    path("authenticated/", is_authenticated),
    path("create_menu/", create_menu, name="create_menu"),
    path("create_category/", create_category, name="create_category"),
    path("get_menu/<str:slug>", get_menu, name="get_menu"),
    path("del_menu/<int:pk>", remove_menu, name="remove_menu"),
    path("get_category/", get_category, name = "get_category"),
    path("add_item/", add_item, name = "additem"),
    path("product_in_cart/", product_in_cart, name = "product_in_cart"),
    path('get_cart/', get_cart, name = 'cartitem'),
    path('delete/<int:pk>', delete_items, name = "deleteitems")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
