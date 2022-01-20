
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('user/', views.user, name="shop"),
    path('login/', views.login, name="login"),
    # path('shops/', views.shop, name="shop"),
    # path('menus/<int:shop>', views.menu, name='menu'),
    # path('order/', views.order, name='order')
    # path('snippets/<int:pk>/', views.snippet_detail),
]
